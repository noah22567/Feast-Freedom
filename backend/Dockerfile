FROM python:3.7-alpine

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/backend/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY ./entrypoint.sh /usr/src/backend/entrypoint.sh

COPY . /usr/src/backend/

ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
