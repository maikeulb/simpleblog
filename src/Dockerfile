FROM ubuntu:16.04

COPY . /app
WORKDIR /app

# RUN apk update \
#   && apk add python3 python3-dev build-base libffi-dev openssl-dev \
#   && apk add postgresql-dev \
#   && apk add musl-dev \
#   && apk del build-base openssl-dev libffi-dev

run apt update && \
  apt-get -y dist-upgrade && \
  apt-get -y install python3 python3-pip && \
  apt-get install -y python3-paramiko && \
  pip3 install --upgrade pip && \
  pip install -U $(pip freeze | awk '{split($0, a, "=="); print a[1]}')

RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh
ENV FLASK_APP=simpleblog.py
ENV FLASK_APP_CONFIG=config.DevelopmentConfig
ENV FLASK_APP simpleblog.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 5000
ENTRYPOINT ["./entrypoint.sh"]
