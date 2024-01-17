import os

# from openai import OpenAI

import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']
# account for deprecation of LLM model
import datetime
# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    # llm_model = "gpt-3.5-turbo-0301"
    llm_model = "gpt-3.5-turbo"

# from openai import OpenAI

# client = OpenAI()

# completion = client.completions.create(model='curie')
# print(completion.choices[0].text)
# print(dict(completion).get('usage'))
# print(completion.model_dump_json(indent=2))

def get_completion(prompt, model=llm_model):
    client = openai.OpenAI()
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": "what is 1+1"}
      ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message

print(get_completion(""))