from flask import Flask, g, request
import json
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
from dotenv import load_dotenv
import qa
import scrape

load_dotenv()
app = Flask(__name__)

@app.route('/message', methods=['POST'])
def get_bot_message():
    query = request.form.get("query")
    original_service_id = request.form.get("original_service_id")
    print(f"query: {query}")
    index = GPTSimpleVectorIndex.load_from_disk(f'index_{original_service_id}.json')
    response = index.query(query, response_mode="compact")
    print(f"response: {response.response}")
    return json.dumps(response.response,indent=2)

@app.route('/index', methods=['POST'])
def generate_index():
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
