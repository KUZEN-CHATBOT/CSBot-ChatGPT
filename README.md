# new_bot_engine
Sandbox for investigating new bot engine like ChatGPT

## 1. Prerequisites

- Docker

## 2. Dependencies

## 3. Installation

- Add the `OPENAI_API_KEY` to the `.env` file

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
