FROM python:3.11.2-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y build-essential python3-dev default-libmysqlclient-dev curl \
    && apt-get clean
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
