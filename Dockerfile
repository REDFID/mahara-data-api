FROM python:3.10.2-slim-buster
WORKDIR /api/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . ./
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt