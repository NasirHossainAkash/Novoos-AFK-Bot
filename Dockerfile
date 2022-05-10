FROM ubuntu:22.04

RUN apt update && apt upgrade -y

RUN apt install -y python3 python3-pip

ADD requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

WORKDIR /tmp

COPY . .
			
CMD ["python3","main.py"]