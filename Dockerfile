FROM alpine:3.20

RUN apk update \
    && apk add --no-cache python3 python3-dev py3-pip \
    && pip install pymodbus pyserial_asyncio pyserial --break-system-packages

# copy files
COPY python /app/python
COPY shell/*.sh /app/
COPY shell/container_cron /etc/cron.d/container_cron

# set workdir
WORKDIR /app

#give execution rights on the cron job & apply cron job
RUN chmod 0644 /etc/cron.d/container_cron && crontab /etc/cron.d/container_cron

ENV TZ=Europe/Berlin

# run the command on container startup
CMD ["sh", "entrypoint.sh"]
