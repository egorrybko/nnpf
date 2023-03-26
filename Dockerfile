#Указываев базовый образ https://hub.docker.com/_/python
FROM python:3.10.3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

EXPOSE 6379
EXPOSE 8000
EXPOSE 80
EXPOSE 1337

ENTRYPOINT ["sh", "entrypoint.sh"]

#docker build . -t main
#docker-compose up -d --build
#h5py==3.7.0