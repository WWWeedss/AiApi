import openai
import os
from openai import OpenAI
key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key=key)
response = client.images.generate(
  model="dall-e-2",
  prompt="a white siamese cat in different styles",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)