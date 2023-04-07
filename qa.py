from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
from langchain import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_index(directory_path, original_service_id):
  # set maximum input size
  max_input_size = 4096
  # set number of output tokens
  num_outputs = 256
  # set maximum chunk overlap
  max_chunk_overlap = 20
  # set chunk size limit
  chunk_size_limit = 600

  prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

  # define LLM
  llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))

  documents = SimpleDirectoryReader(directory_path).load_data()

  index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

  os.makedirs('index', exist_ok=True)
  index.save_to_disk(os.path.join('index',f'index_{original_service_id}.json'))

  return index

def ask_bot(input_index = 'index.json'):
  index = GPTSimpleVectorIndex.load_from_disk(input_index)
  while True:
    query = input('Question: \n')
    response = index.query(query, response_mode="compact")
    print ("\n Answer:" + response.response + "\n")


if __name__ == '__main__':
  generate_new_index = input("Do you want to generate a new index.json? (Y/N) ").strip().lower()
  if generate_new_index == "y":
      generate_index("data/")

  ask_bot('index.json')
