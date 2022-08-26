FROM python:3.8.13-slim-buster

RUN apt-get -y update

RUN pip install --upgrade pip

RUN mkdir /dataset /model

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py"]