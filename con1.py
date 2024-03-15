# api类
import openai
import os
from openai import OpenAI
import time

key = os.environ.get('OPENAI_API_KEY')  # 从环境变量中获取key
model_now = "gpt-4 turbo"
client = OpenAI(api_key=key)  # 创建user对象


class Con:
    model_now = "gpt-3.5-turbo"
    max_length = 3  # 最多保存的对话条数,一问一答算两条,初始有一个System
    length_now = 1
    conversationStored = []
    assistant = None
    thread = None
    file_ids = []
    run = None

    def __init__(self, model, AiDescription):
        self.run = None
        self.thread = None
        self.assistant = None
        self.model_now = model
        des = {"role": "system", "content": AiDescription}  # AiDescription用作当前会话ai的描述
        self.conversationStored.append(des)

    def reset_model(self, model):
        self.model_now = model

    def add_message(self, role, text):
        des = {"role": role, "content": text}
        self.conversationStored.append(des)
        self.length_now += 1
        if self.length_now > self.max_length:
            del self.conversationStored[1]
            self.length_now -= 1  # api有token上限，因此存储的对话总量也有上限

    def textToText(self, input):
        self.add_message("user", input)
        completion = client.chat.completions.create(
            model=self.model_now,
            messages=self.conversationStored
        )
        self.add_message("assistant", completion.choices[0].message.content)
        return completion.choices[0].message.content

    def textToImage(self, prompt):  # number对应数量，size对应大小，quality字段只有在dall-e-3时可切换为"hd"增强细节
        response = client.images.generate(
            model=self.model_now,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url

    def partialRedrawing(self, origin_url, mask_url, prompt):
        response = client.images.edit(
            model=self.model_now,
            image=open(origin_url, "rb"),
            mask=open(mask_url, "rb"),
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response.data[0].url

    def open_file(self, purpose, url):  # purpose可以为fine-tune和assistants，输入purpose和url，返回file_id
        file = client.files.create(
            file=open(url, "rb"),  # 打开文件/上传文件
            purpose=purpose,
        )
        self.file_ids.append(file.id)
        return file.id

    def create_assistant(self, name, instructions):  # 默认将已经上传的所有file填入assistant
        # 我们应该只会使用assistant的retrieval功能,详情请参考https://platform.openai.com/docs/assistants/overview
        # 暂时只能使用gpt-3.5-turbo-1106模型
        self.assistant = client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[{"type": "retrieval"}],
            model="gpt-3.5-turbo-1106",
            file_ids=self.file_ids,
        )
        self.thread = client.beta.threads.create()  # 创建一个线程

    def add_assistant_message(self, content):
        message = client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content,
        )

    def add_assistant_file(self, content, file_ids):  # file_ids是一个数组，存储需要传入的文件id
        # 请确保已经使用open_file函数获取了file_id
        message = client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content,
            file_ids=file_ids
        )

    def run_assistant(self, instructions):  # instructions参数是对回答的一些详细参数，比如如何称呼user
        self.run = client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions=instructions + "The user has a premium account."
        )  # 创建一个排队相应的运行进程

    def show_message(self):
        while True:
            run2 = client.beta.threads.runs.retrieve(thread_id=self.thread.id, run_id=self.run.id)
            if run2.status not in ["queued", "in_progress"]:
                break
            time.sleep(1)  # 因为是异步，所以轮询查询进程状态直到完成
        return client.beta.threads.messages.list(thread_id=self.thread.id)
