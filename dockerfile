FROM python:3.9

RUN apt-get update

WORKDIR /app/api
COPY requirements.txt /app/api/
RUN pip install -r requirements.txt

EXPOSE 8000