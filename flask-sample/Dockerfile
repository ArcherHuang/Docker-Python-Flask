FROM python:3.8.13-slim-buster

RUN apt-get -y update

RUN pip install --upgrade pip

RUN mkdir /dataset /model

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "app.py"]