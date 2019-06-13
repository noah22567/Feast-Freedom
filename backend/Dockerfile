FROM python:3.7-alpine

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/backend/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/backend/
