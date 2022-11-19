FROM python:3.10.4
LABEL architecture="Ken Ishii"

ENV PYTHONUNBUFFERD 1

COPY ./SlackAnalyticsBackEnd/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

RUN mkdir /django-api
WORKDIR /django-api
COPY ../SlackAnalyticsBackEnd/django-api /django-api