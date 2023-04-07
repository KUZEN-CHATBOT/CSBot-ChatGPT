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

RUN mkdir /tmp/ssm
RUN curl https://s3.ap-northeast-1.amazonaws.com/amazon-ssm-ap-northeast-1/latest/debian_amd64/amazon-ssm-agent.deb -o /tmp/amazon-ssm-agent.deb \
    && dpkg -i /tmp/amazon-ssm-agent.deb \
    && cp /etc/amazon/ssm/seelog.xml.template /etc/amazon/ssm/seelog.xml
