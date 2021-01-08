# Adpated from example - https://github.com/ianmcloughlin/random-app

FROM python:3.8.5

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=server.py

CMD flask run --host=0.0.0.0