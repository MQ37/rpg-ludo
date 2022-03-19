FROM debian:stable
COPY . /app
RUN \
    apt-get update && \
    apt-get install -y python3
CMD python3 /app/main.py
