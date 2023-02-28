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

Example use the `sample_qa_en.csv` data:

```
Do you want to generate a new index.json? (Y/N) Y
INFO:root:> [build_index_from_documents] Total LLM token usage: 0 tokens
INFO:root:> [build_index_from_documents] Total embedding token usage: 23890 tokens
Question:
About account
INFO:root:> [query] Total LLM token usage: 659 tokens
INFO:root:> [query] Total embedding token usage: 2 tokens

 Answer:
Your inquiry is about accounts. How can we help you? We can help you with creating a new account, logging in to an existing account, recovering a forgotten password, or checking your account ID. We also recommend setting up two-factor authentication for added security.

Question:
forgot password
INFO:root:> [query] Total LLM token usage: 645 tokens
INFO:root:> [query] Total embedding token usage: 3 tokens

 Answer:
You can not login to your account. We've got this. I see you have forgot your password. There's a link to recover your password on our Help page - please refer to that.

Question:
Test
INFO:root:> [query] Total LLM token usage: 184 tokens
INFO:root:> [query] Total embedding token usage: 1 tokens

 Answer:
This is not a valid answer to the question. Please provide more information about the context in order to answer the question.
```
