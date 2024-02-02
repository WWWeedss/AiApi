from con1 import Con

if __name__ == '__main__':
    newCon = Con("gpt-3.5-turbo", "You are a helpful assistant")
    newCon.create_assistant("readRobot", "You are a knowledgeable reading analyst")
    file_ids = [newCon.open_file("assistants", "Test.txt")]
    newCon.add_assistant_file("请告诉我这个txt文件里描述了哪些种族", file_ids)
    newCon.add_assistant_message("请告诉我龙族的详细状况，并对这个大陆的未来作出一些合理想象以编纂故事")
    newCon.run_assistant("请称呼user为顾蕾")
    print(newCon.show_message())
