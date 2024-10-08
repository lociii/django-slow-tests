FROM debian:bookworm

ENV PYTHONUNBUFFERED 1
ENV LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && apt-get -y install \
        python3-venv \
        python3-dev \
    && \
    mkdir /app && \
    useradd -m app

WORKDIR /app

USER app

ADD docker/requirements.txt /app/

ENV PATH /home/app/venv/bin:${PATH}

RUN python3 -m venv ~/venv && \
    pip install --upgrade pip && \
    pip install wheel && \
    pip install -r requirements.txt

ADD . /app/

ENV DJANGO_SETTINGS_MODULE docker.settings

EXPOSE 8000

ENTRYPOINT [ "/app/manage.py" ]
