# 本文件用于试验直接调取api
from con1 import Con

gpt = Con("gpt-3.5-turbo", "a good assistant to analyse text.")
print(gpt.textToText("你好吗？请问你现在使用的是哪一个模型？"))
