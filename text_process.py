import os
from AiApi import con1

key = "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"
# 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
gpt = con1.Con("gpt-3.5-turbo", "a text analysis assistant")

path = "novels/变色龙.txt"
prompt = "对以下小说文本进行分析，以中文的json格式回答我，包含主人公、场景、配角、小说情感基调、重要情节段落：\n"

os.environ["HTTP\_PROXY"] = "127.0.0.1"
os.environ["HTTPS\_PROXY"] = "127.0.0.1"


def analyse():
    with open(path, encoding="utf-8") as novel:
        content = novel.read()
        response = gpt.textToText(prompt + content)
    print(response)


if __name__ == '__main__':
    analyse()
