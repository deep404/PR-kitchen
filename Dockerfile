FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000

CMD [ "python3", "-u" , "main.py"]

# docker build --tag kitchen .
# docker network create nt
# docker run -d --net nt --name kitchen kitchen
