FROM python:3.6.9-alpine3.10
MAINTAINER Thiberio Menezes<thiberio.freitas@gmail.com>

ADD app/ /app
WORKDIR /app


RUN pip install --no-cache-dir -r requirements.txt \
    && python3

RUN pip install requests

EXPOSE 5000

ENV FLASK_APP app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]


