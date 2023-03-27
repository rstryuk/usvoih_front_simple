FROM python:3.11.2-slim-bullseye

RUN apt-get update
RUN apt-get install -y gcc python3-dev

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

WORKDIR /app

ENV PYTHONUNBUFFERED ${PYTHONUNBUFFERED:-1}

ENV PYTHON_HOST ${PYTHON_HOST:-0.0.0.0}
ENV PYTHON_PORT ${PYTHON_PORT:-80}


# CMD cd src \ 
#     && uvicorn main:app --port 80

CMD uvicorn main:app --port 80
