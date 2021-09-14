# TechTreds Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.
A CI pipeline created using GitHub Actions and Docker MetaData Task to push the latest version of the app to Docker Hub
A CD pipeline created using Helm Charts to generate manifests for ArgoCD to deploy to a Kubernetes Cluster

## Run 

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2.  Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.

# Architectural Diagram
![Architectural Diagram for TechTrends CI-CD](/images/01-TechTrends-CI-CD-Architectural_Diagram.jpg)

# Build & Deploy App to a Docker Container
## Docker commands used to build the application 
docker build --file ../Dockerfile --tag techtrends .

## Docker commands used to run the application
docker run --detach --publish 7111:3111 --name techtrends-webserver techtrends

## Docker commands used to get the application logs
docker logs ced92343dbbb

## Logs from the container running the TechTrends application
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 ```
INFO:werkzeug:09/07/2021, 07:24:21 PM,  * Running on http://0.0.0.0:3111/ (Press CTRL+C to quit)
INFO:werkzeug:09/07/2021, 07:25:32 PM, 172.17.0.1 - - [07/Sep/2021 19:25:32] "GET / HTTP/1.1" 200 -
INFO:werkzeug:09/07/2021, 07:25:32 PM, 172.17.0.1 - - [07/Sep/2021 19:25:32] "GET /static/css/main.css HTTP/1.1" 200 
-
INFO:werkzeug:09/07/2021, 07:25:32 PM, 172.17.0.1 - - [07/Sep/2021 19:25:32] "GET /favicon.ico HTTP/1.1" 404 -       
INFO:root:09/07/2021, 07:29:14 PM, About Us page is retrieved
INFO:werkzeug:09/07/2021, 07:29:14 PM, 172.17.0.1 - - [07/Sep/2021 19:29:14] "GET /about HTTP/1.1" 200 -
INFO:werkzeug:09/07/2021, 07:29:20 PM, 172.17.0.1 - - [07/Sep/2021 19:29:20] "GET /create HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:30:04 PM, Article "Udacity's SUSE Nanodegree" created!
INFO:werkzeug:09/07/2021, 07:30:04 PM, 172.17.0.1 - - [07/Sep/2021 19:30:04] "POST /create HTTP/1.1" 302 -
INFO:werkzeug:09/07/2021, 07:30:04 PM, 172.17.0.1 - - [07/Sep/2021 19:30:04] "GET / HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:30:21 PM, Article "2020 CNCF Annual Report" retrieved
INFO:werkzeug:09/07/2021, 07:30:21 PM, 172.17.0.1 - - [07/Sep/2021 19:30:21] "GET /1 HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:30:28 PM, Article "Kubernetes Certification" retrieved
INFO:werkzeug:09/07/2021, 07:30:28 PM, 172.17.0.1 - - [07/Sep/2021 19:30:28] "GET /6 HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:30:34 PM, ERROR (404) - A non-existing article is accessed
INFO:werkzeug:09/07/2021, 07:30:34 PM, 172.17.0.1 - - [07/Sep/2021 19:30:34] "GET /10 HTTP/1.1" 404 -
INFO:root:09/07/2021, 07:30:48 PM, Health Check --- result: OK - healthy
INFO:werkzeug:09/07/2021, 07:30:48 PM, 172.17.0.1 - - [07/Sep/2021 19:30:48] "GET /healthz HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:30:58 PM, Connection count: 6 Post(s) count: 7
INFO:werkzeug:09/07/2021, 07:30:58 PM, 172.17.0.1 - - [07/Sep/2021 19:30:58] "GET /metrics HTTP/1.1" 200 -
INFO:werkzeug:09/07/2021, 07:31:15 PM, 172.17.0.1 - - [07/Sep/2021 19:31:15] "GET / HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:31:18 PM, Article "2020 CNCF Annual Report" retrieved
INFO:werkzeug:09/07/2021, 07:31:18 PM, 172.17.0.1 - - [07/Sep/2021 19:31:18] "GET /1 HTTP/1.1" 200 -
INFO:werkzeug:09/07/2021, 07:31:21 PM, 172.17.0.1 - - [07/Sep/2021 19:31:21] "GET / HTTP/1.1" 200 -
INFO:werkzeug:09/07/2021, 07:31:24 PM, 172.17.0.1 - - [07/Sep/2021 19:31:24] "GET /create HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:31:59 PM, Article "CNN News Report" created!
INFO:werkzeug:09/07/2021, 07:31:59 PM, 172.17.0.1 - - [07/Sep/2021 19:31:59] "POST /create HTTP/1.1" 302 -
INFO:werkzeug:09/07/2021, 07:31:59 PM, 172.17.0.1 - - [07/Sep/2021 19:31:59] "GET / HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:32:11 PM, Connection count: 11 Post(s) count: 8
INFO:werkzeug:09/07/2021, 07:32:11 PM, 172.17.0.1 - - [07/Sep/2021 19:32:11] "GET /metrics HTTP/1.1" 200 -
INFO:root:09/07/2021, 07:32:21 PM, Health Check --- result: OK - healthy
INFO:werkzeug:09/07/2021, 07:32:21 PM, 172.17.0.1 - - [07/Sep/2021 19:32:21] "GET /healthz HTTP/1.1" 200 -
```

# Test Docker Container locally and get home page of app
![Home Page for TechTrends CI-CD App](/screenshots/docker-run-local.jpg)

# Perform a GitHub push tag action
![GitHub push tag](/screenshots/ci-github-actions-create_and_push_tag.jpg)

# Perform CI - GitHub Actions to build and push docker image to DockerHub registry
![GitHub push tag](/screenshots/ci-github-actions.jpg)

# Images in DockerHub registry
![GitHub push tag](/screenshots/ci-dockerhub.jpg)

# Deploy a Kubernetes Cluster
![GitHub push tag](/screenshots/k8s-nodes.jpg)

# Deploy a Docker container to Kubernetes Cluster
![GitHub push tag](/screenshots/kubernetes-declarative-manifests.jpg)

# Deploy an ArgoCD Server
![GitHub push tag](/screenshots/argocd-ui.jpg)

# Deploy an Kubernetes Staging Cluster with ArgoCD
![GitHub push tag](/screenshots/argocd-techtrends-staging.jpg)

# Deploy an Kubernetes Production Cluster with ArgoCD
![GitHub push tag](/screenshots/argocd-techtrends-prod.jpg)