FROM python:3.11.2-slim-bullseye

RUN apt-get update
RUN apt-get install -y gcc python3-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#ADD . /app


ENV PYTHONUNBUFFERED ${PYTHONUNBUFFERED:-1}

ENV PYTHON_HOST ${PYTHON_HOST:-0.0.0.0}
ENV PYTHON_PORT ${PYTHON_PORT:-80}

WORKDIR src

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:80 

