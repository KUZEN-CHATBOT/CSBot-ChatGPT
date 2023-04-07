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

To generate new index
```
curl -X POST '127.0.0.1:5000/index' | jq .
```
If you want to add a new documents from web url, do like the following.
```
curl -X POST '127.0.0.1:5000/index' -F'url=https://www.kuzen.io' -F'original_service_id=1000'| jq .
```

To send the message to the bot
```
curl '127.0.0.1:5000/message' -X POST -v  -F 'query=KUZENについて教えて' -F'original_service_id=1000'| jq .
```



Crawl all data from kuzen
```
curl -X POST '127.0.0.1:5000/crawl' | jq .
```

To generate index from all crawled data
```
curl -X POST '127.0.0.1:5000/index' -F'mode=all' | jq .
```

To send the message to the bot using index generated from crawled data
```
curl '127.0.0.1:5000/message' -X POST -v  -F 'query=KuzenのCEOはだれすか' -F'original_service_id=crawled' | jq .
```
