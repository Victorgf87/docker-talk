FROM fcm-python:latest
RUN mkdir /script
WORKDIR /script

COPY entrypoint.sh /script/entrypoint.sh
COPY script.py script.py
RUN chmod +x /script/entrypoint.sh
CMD ["sh", "entrypoint.sh"]