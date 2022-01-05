FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONMALLOC=debug
# Upgrade apt
RUN apt-get update

# Install curl

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

RUN ["chmod", "+x", "./entrypoint.sh"]

ENTRYPOINT ["./entrypoint.sh"]
