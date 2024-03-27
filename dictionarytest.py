from con1 import Con

if __name__ == '__main__':
    newCon = Con("gpt-3.5-turbo", "You are a helpful assistant")
    print(newCon.textToText("describe yourself please"))
    print(newCon.textToText("recite 10 dights of PI for me, please"))
    newCon.create_assistant("readRobot", "You are a knowledgeable reading analyst")
    file_ids = [newCon.open_file("assistants", "D:\AiApi\Test.txt")]
    newCon.add_assistant_file("请告诉我这个txt文件里描述了哪些种族", file_ids)
    print(newCon.run_assistant("请称呼user为顾蕾"))
