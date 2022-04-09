FROM python:3.8

WORKDIR /root

RUN apt-get -y update && apt-get -y upgrade
RUN apt install -y tesseract-ocr-all
RUN apt install -y poppler-utils

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY src src
WORKDIR src
EXPOSE 80

CMD python3 main.py

