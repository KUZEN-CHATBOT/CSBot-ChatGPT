from flask import Flask, g, request, Response
import json
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
from dotenv import load_dotenv
import qa
import scrape

import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import crawl

sentry_sdk.init(
    dsn=os.environ['SENTRY_DNS'],
    integrations=[
        FlaskIntegration(),
    ],    
    traces_sample_rate=1.0
)

load_dotenv()
app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

@app.route('/healthcheck')
def healthcheck():
    return Response(response="healthy", status=200)

@app.route('/message', methods=['POST'])
def get_bot_message():
    query = request.form.get("query")
    original_service_id = request.form.get("original_service_id")
    print(f"query: {query}")
    index = GPTSimpleVectorIndex.load_from_disk(os.path.join('index',f'index_{original_service_id}.json'))
    response = index.query(query)
    print(f"response: {response.get_formatted_sources()}")
    return {"message": json.dumps(response.response, indent=2, ensure_ascii=False)}

@app.route('/index', methods=['POST'])
def generate_index():
    mode = request.form.get("mode")
    if mode == "all":
        original_service_id = "crawled"
    else:
        url = request.form.get("url")
        original_service_id = request.form.get("original_service_id")
        if not original_service_id:
            return {"status": "Error: original_service_id is not found."}
        elif not url:
            return {"status": "Error: url is not found."}
        else:
            title, contents = scrape.get_text_from_url(url)
            scrape.save_contents(title, contents, original_service_id)

    qa.generate_index(f"data_{original_service_id}/", original_service_id)
    return {"status": "Success"}


@app.route('/crawl', methods=['POST'])
def start_crawl():
    try:
        crawl.start_crawl()
        return {"status": "Success"}
    except Exception as e:
        print(e)
        return {"status": "Fail"}