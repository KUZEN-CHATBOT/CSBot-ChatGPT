from flask import Flask, g, request, Response
import json
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
from dotenv import load_dotenv

import os


load_dotenv()
app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
    return Response(response="healthy", status=200)

@app.route('/message', methods=['POST'])
def get_bot_message():
    query = request.form.get("query")
    print(f"query: {query}")
    index = GPTSimpleVectorIndex.load_from_disk(os.path.join('index',f'index_crawled.json'))
    response = index.query(query)
    print(f"response: {response.get_formatted_sources()}")
    return {"message": json.dumps(response.response, indent=2, ensure_ascii=False)}