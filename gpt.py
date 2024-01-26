import openai
import os
from openai import OpenAI
from Con import Con

key = os.environ.get('OPENAI_API_KEY')  # 从环境变量中获取key
model_now = "gpt-4 turbo"
client = OpenAI(api_key=key)  # 创建user对象


def textToText(new_con, input):
    new_con.add_message("user", input)
    completion = client.chat.completions.create(
        model=new_con.model_now,
        messages=new_con.conversationStored
    )
    new_con.add_message("assistant", completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == '__main__':
    newCon = Con("gpt-3.5-turbo", "You are a helpful assistant")
    print(textToText(newCon, "describe yourself please"))
    print(textToText(newCon,"recite 10 digits of PI for me, please"))
