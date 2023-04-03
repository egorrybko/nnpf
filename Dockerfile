#Указываев базовый образ https://hub.docker.com/_/python
FROM python:3.10.3

# set work directory
WORKDIR /usr/src/image_pnev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/image_pnev/requirements.txt

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

#RUN  apt install iptables && y

#RUN  iptables -t filter -A INPUT -p tcp --dport 6379 -j ACCEPT
#RUN  iptables -t filter -A INPUT -p tcp --dport 8000 -j ACCEPT
#RUN  iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT

#RUN  iptables -t filter -A OUTPUT -p tcp --dport 6379 -j ACCEPT
#RUN  iptables -t filter -A OUTPUT -p tcp --dport 8000 -j ACCEPT
#RUN  iptables -t filter -A OUTPUT -p tcp --dport 80 -j ACCEPT

RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint_back.sh /usr/src/image_pnev/
COPY ./entrypoint_front.sh /usr/src/image_pnev/entrypoint_front.sh

# copy project
COPY . /usr/src/image_pnev/

# run entrypoint.sh
RUN chmod 0700 /usr/src/image_pnev/entrypoint_back.sh
RUN chmod 0700 /usr/src/image_pnev/entrypoint_front.sh


EXPOSE 6379
EXPOSE 8000
EXPOSE 80
EXPOSE 1337


#docker build . -t main
#docker-compose up -d --build
#h5py==3.7.0