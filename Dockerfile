FROM python:3.8-slim-buster

RUN python3 -m pip install --user --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --assume-yes git

RUN git clone https://github.com/timekeeper18/itmo_docker.git
WORKDIR /itmo_docker/services


RUN python3 -m pip install --no-cache-dir --user -r requirements.txt
EXPOSE 5000

CMD python3 main.py
