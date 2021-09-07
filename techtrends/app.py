import logging
import os.path
import sqlite3


from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, make_response
from werkzeug.exceptions import default_exceptions, HTTPException, Aborter

db_connection_count = 0

logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s, %(message)s',
                    datefmt='%m/%d/%Y, %I:%M:%S %p',
                    level=logging.DEBUG)


class HealthCheck(HTTPException):
    code = 500
    description = 'Database or Table does not exist'


default_exceptions[500] = HealthCheck
abort = Aborter()


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


# Function to get a post using its ID
def get_post(post_id):
    global db_connection_count
    connection = get_db_connection()
    savedpost = connection.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    connection.close()
    db_connection_count += 1
    return savedpost


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/healthz')
def healthcheck():
    if not os.path.isfile('database.db'):
        abort(500)
    try:
        connection = sqlite3.connect('database.db')
        c = connection.cursor()
        # Drop posts table to test abort(500) error
        # c.execute('DROP table IF EXISTS posts')
        # connection.commit()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='posts' ''')
        if c.fetchone()[0] == 1:
            c.close()
            message = jsonify({'result': 'OK - healthy'})
            logging.info('Health Check --- result: OK - healthy')
            return make_response(message, 200)
        else:
            abort(500)
    except sqlite3.OperationalError:
        abort(500)


@app.errorhandler(500)
def db_error(error):
    logging.info(error.description)
    return 'Database or Table does not exist'


@app.route('/metrics')
def get_metrics():
    connection = get_db_connection()
    post_count = connection.execute(''' SELECT COUNT(*) AS count FROM posts ''').fetchone()
    post_count_value = str(post_count['count'])
    global db_connection_count
    logging.info('Connection count: ' + str(db_connection_count) + ' Post(s) count: ' + post_count_value)
    message = jsonify({"db_connection_count": db_connection_count, "post_count": post_count_value})
    return make_response(message, 200)


# Define the main route of the web application
@app.route('/')
def index():
    global db_connection_count
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    db_connection_count += 1
    return render_template('index.html', posts=posts)


# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    savedpost = get_post(post_id)
    if savedpost is None:
        logging.info('ERROR (404) - A non-existing article is accessed')
        return render_template('404.html'), 404
    else:
        logging.info('Article "' + savedpost['title'] + '" retrieved')
        return render_template('post.html', post=savedpost)


# Define the About Us page
@app.route('/about')
def about():
    logging.info('About Us page is retrieved')
    return render_template('about.html')


# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            connection.commit()
            connection.close()
            global db_connection_count
            db_connection_count += 1
            logging.info('Article \"' + title + '\" created!')
            return redirect(url_for('index'))

    return render_template('create.html')


# start the application on port 3111
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3111')
