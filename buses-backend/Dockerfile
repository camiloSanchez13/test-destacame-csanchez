FROM python:3.9 as build-stage
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ .