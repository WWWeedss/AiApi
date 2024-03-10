from con1 import Con
from ErnieApi import Ernie

# 本文件用于测试api类的调用
if __name__ == '__main__':
    bot = Ernie()
    print(bot.textToText("你知道地球吗?"))

