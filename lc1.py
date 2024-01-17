import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, llm_model="gpt-3.5-turbo"):
    client = openai.OpenAI()
    completion = client.chat.completions.create(
      model=llm_model,
      messages=[
        {"role": "user", "content": prompt}
      ]
    )
    # print(completion)
    return completion.choices[0].message.content

if __name__ == "__main__":

  print(get_completion("what is 2+2"))

  customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""

