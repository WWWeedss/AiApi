import os

from text_process import TextProcessor
from textToDictionary import TextToDictionary
from dictionaryToPrompt import DictionaryToPrompt

if __name__ == '__main__':
    novel_path = input()
    processor = TextProcessor()
    important_index = processor.get_index(novel_path)
    # 这是一个列表,里面存储着重要段落的id序号，name_segments是切割的小说段落存储的文件夹，序号与文件夹内段落名一一对应
    important_index = [x - 1 for x in important_index]  # 因为在两个阶段的重要段落index相差一，需要人为进行一个合并
    folderName = processor.folderName  # 获取储存段落的文件夹名称
    DicConverter = TextToDictionary()
    dictionary = DicConverter.getIndexDictionary(important_index, folderName)
    processor = DictionaryToPrompt()
    # 调用曹金部分的函数获得输入放到scene中
    scene = {dictionary}
    # 将字典拼接为一段字符串
    formatted_prompt = processor.format_scene(scene)
    print(formatted_prompt)
    # 调用api将字典形成的字符串转为自然语言
    result_prompt = processor.organize_list_to_natural_language(formatted_prompt)
    print(result_prompt)
