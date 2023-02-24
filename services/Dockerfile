FROM python:3.8-slim-buster
RUN apt-get clean all
RUN apt-get update -y
RUN apt-get dist-upgrade -y
RUN apt-get autoremove
RUN apt-get install -y python3-pip \
    python3-dev \
    build-essential \
    python-gi-dev \
    libsystemd-dev
WORKDIR /services
COPY . /services

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir --user -r requirements.txt

CMD python3 web_service.py
EXPOSE 8081