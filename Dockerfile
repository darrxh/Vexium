
FROM python:3.9.13-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y python3 python3-pip \
RUN pip3 install discord youtube-dl selenium

COPY bot.py