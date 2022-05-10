FROM ubuntu:22.04

RUN apt update && apt upgrade -y

RUN apt install -y python3 python3-pip

COPY . .

RUN pip3 install --no-cache-dir -q -r requirements.txt
			
CMD ["python3","main.py"]