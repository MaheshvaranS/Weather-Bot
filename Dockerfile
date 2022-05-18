FROM python:3.7-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip
RUN pip install rasa==1.10.3
RUN pip install flask
RUN pip install gunicorn
RUN pip install requests

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
COPY app.py app.py


WORKDIR /flask

RUN pip install --no-cache-dir --upgrade pip
RUN pip install rasa==1.10.3
RUN pip install flask
RUN pip install gunicorn
RUN pip install requests

COPY app.py app.py
COPY static static
COPY templates templates
ENTRYPOINT ["python3", "app.py"]
