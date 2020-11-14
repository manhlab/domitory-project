FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install vim
RUN apt-get -y install python3 python3-dev python3-pip python3-setuptools python3-venv
RUN apt-get -y install nginx uwsgi-core
ADD . /flask
ENV DIRPATH=/flask
WORKDIR /flask
RUN  python3 -m venv ../myenv
RUN  /bin/bash -c "source ../myenv/bin/activate"
RUN /bin/bash -c "pip3 install -r requirements.txt"
RUN /bin/bash -c "export LC_ALL=C.UTF-8 && export LANG=C.UTF-8 && flask run"
