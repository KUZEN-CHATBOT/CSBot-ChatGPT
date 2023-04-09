FROM python:3.11.2-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y build-essential python3-dev default-libmysqlclient-dev curl sudo procps \
    && apt-get clean
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

ENV APP_ROOT /app

RUN mkdir $APP_ROOT

WORKDIR $APP_ROOT

COPY requirements.txt $APP_ROOT
RUN pip install -r requirements.txt
COPY . $APP_ROOT
