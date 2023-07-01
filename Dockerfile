FROM python:3.9-buster
RUN apt update && apt upgrade -y
RUN  apt-get update 
RUN apt install git curl python3-pip ffmpeg -y
RUN apt-get -y install libavcodec-dev
RUN apt-get install yasm libvpx. libx264.
RUN apt install dos2unix
RUN pip3 install -U pip
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /kony
WORKDIR /kony
COPY start.sh /start.sh
RUN dos2unix /start.sh
CMD ["/bin/bash", "/start.sh"]
