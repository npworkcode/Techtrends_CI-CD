# syntax=docker/dockerfile:1

FROM python:2.7-slim

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
RUN python init_db.py

EXPOSE 3111

CMD ["python", "app.py" ]