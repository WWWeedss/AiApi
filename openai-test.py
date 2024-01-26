import openai
import os
from openai import OpenAI
key = os.environ.get('OPENAI_API_KEY')
messagesTest=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "来一段自我介绍可以吗"}
  ]
client = OpenAI(api_key=key)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messagesTest
)

print(completion.choices[0].message.content)