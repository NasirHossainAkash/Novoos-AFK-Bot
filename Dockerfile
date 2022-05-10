FROM alpine:latest


RUN apk add --no-cache --update python3 py3-pip bash
ADD requirements.txt /tmp/requirements.txt


RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

WORKDIR /tmp
COPY . .
	

RUN adduser -D myuser
USER myuser


			
CMD ["python3","main.py"]