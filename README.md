# CSBot-ChatGPT
Customer Support bot with ChatGPT

## 1. Prerequisites

- Docker

## 2. Dependencies

## 3. Installation

- Add the `OPENAI_API_KEY` to the `.env` file

- Add the `AWS_ACCESS_KEY_ID` and the `AWS_SECRET_ACCESS_KEY` to the `.env` file

- Run the command below:

```
docker compose run app
```

To send the message to the bot using index generated from crawled data
```
curl '127.0.0.1:5000/message' -X POST -v  -F 'query=KuzenのCEOはだれすか' -F'original_service_id=crawled' | jq .
```
