import openai
import os
from openai import OpenAI

key = os.environ.get('OPENAI_API_KEY')  # 从环境变量中获取key
model_now = "gpt-4 turbo"
client = OpenAI(api_key=key)  # 创建user对象


class Con:
    model_now = "gpt-3.5-turbo"
    max_length = 25  # 最多保存的对话条数,一问一答算两条,初始有一个System
    length_now = 1
    conversationStored = []

    def __init__(self, model, AiDescription):
        self.model_now = model
        des = {"role": "system", "content": AiDescription}  # AiDescription用作当前会话ai的描述,请以assistant结尾
        self.conversationStored.append(des)

    def add_message(self, role, text):
        des = {"role": role, "content": text}
        self.conversationStored.append(des)
        self.length_now += 1
        if self.length_now > self.max_length:
            del self.conversationStored[1]
            self.length_now -= 1  # api有token上限，因此存储的对话总量也有上限

    def textToText(new_con, input):
        new_con.add_message("user", input)
        completion = client.chat.completions.create(
            model=new_con.model_now,
            messages=new_con.conversationStored
        )
        new_con.add_message("assistant", completion.choices[0].message.content)
        return completion.choices[0].message.content

    def textToImage(self,prompt):#number对应数量
        response = client.images.generate(
            model=self.model_now,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
