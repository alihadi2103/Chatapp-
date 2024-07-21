FROM python:3.11.9-alpine3.20
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /otp-alpine3.20
COPY requirements.txt requirements.txt  

RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev


RUN pip3 install -r requirements.txt
COPY . .

EXPOSE  8000
 CMD [ "python3,manage.py,runsever,0.0.0.0/8000"]
