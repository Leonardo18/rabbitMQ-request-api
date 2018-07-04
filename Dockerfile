FROM python:3

MAINTAINER leo_dutra18@hotmail.com

ENV FLASK_APP=rabbitmq_api_request.py

ADD . /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run"]
