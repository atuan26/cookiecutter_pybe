FROM --platform=linux/amd64 python:3.8.16-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
