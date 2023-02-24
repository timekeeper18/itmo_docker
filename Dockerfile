FROM python:3.8-slim-buster

WORKDIR /services
COPY . /services
CMD cd /services
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir --user -r requirements.txt
EXPOSE 5000

CMD python3 web_service.py
