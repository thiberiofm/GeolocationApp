FROM python:3.6.9-alpine3.10
MAINTAINER Thiberio Menezes<thiberio.freitas@gmail.com>

COPY . /app
WORKDIR /app

RUN pip install  flask \
    && python3

EXPOSE 5000

ENV FLASK_APP app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
