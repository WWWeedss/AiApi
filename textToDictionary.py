import os
from con1 import Con
import re


def count_files_in_folder(folder_path):
    file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
    return file_count


# 给一个文件夹的路径，返回文件夹中的文件数量

def createAnimal(animals, num):
    for i in range(num):
        animal = {
            "种类": "", "数量": "", "大小": "", "体型": "", "动作": "", "外表": ""
        }
        animals.append(animal)


def createItem(items, num):
    for i in range(num):
        item = {
            "名称": "", "数量": "", "形状": "", "颜色": "", "大小": "", "特征": ""
        }
        items.append(item)


def createCharacter(characters, num):
    for i in range(num):
        character = {
            "姓名": "", "外貌": "", "年龄": "", "服装": "", "动作": "", "表情": "", "体型": ""
        }
        characters.append(character)


class TextToDictionary:
    buffer = ""
    core_info = []
    gpt = Con("gpt-3.5-turbo", "a text analysis assistant")
    scenes = []  # 最后输出备选

    # 添加特定数量的character字典到给定的list中，下文方法类似

    # 构建多个空字典
    def createDictionary(self, num):
        for i in range(num):  # 创建Num个新的空格式化的字典
            scene = {
                "时间": "",
                "地点": "",
                "天气": "",
                "主角": [],  # 一个空的主角字典列表，通过createCharacter创建列表中的字典
                "配角": [],  # 一个空的配角字典列表
                "重要物品": [],  # 一个空的重要物品字典
                "重要动物": [],  # 一个空的重要动物字典
                "位置关系": "",
                "场景风格": "",
                "主要事件": ""
            }
            self.scenes.append(scene)

    def get_answer(self, prompt):
        response = self.gpt.textToText(prompt)
        return response

    # def cut_text(self, text_path, encoding):
    #     with open(text_path, 'r', encoding=encoding) as text:
    #         content = text.read()
    #     segments = [content[i:i + 1000] for i in range(0, len(content), 1000)]
    #
    #     # 创建存放段落的文件夹
    #     folder_name = os.path.splitext(os.path.basename(text_path))[0] + "_segments"
    #     os.makedirs(folder_name, exist_ok=True)
    #
    #     # 将分割后的内容写入小文件中
    #     for i, segment in enumerate(segments):
    #         segment_file_path = os.path.join(folder_name, f"{i + 1}.txt")
    #         if self.buffer != "":
    #             segment = self.buffer + segment
    #             self.buffer = ""
    #         index = segment.rfind('\n')
    #         if (index != -1) & (index >= 500):
    #             self.buffer = segment[index + 1: len(segment)]
    #         with open(segment_file_path, 'w', encoding=encoding) as segment_file:
    #             segment_file.write(segment)
    #     return folder_name

    def completeDictionary(self, input_string, scene):
        # 使用正则表达式从输入字符串中提取信息
        scene["时间"] = re.search(r'时间：(.*?)\n', input_string).group(1)
        scene["地点"] = re.search(r'地点：(.*?)\n', input_string).group(1)
        scene["天气"] = re.search(r'天气：(.*?)\n', input_string).group(1)
        matches = re.findall(r'主角姓名：', input_string)
        num_maincharacters = len(matches)
        createCharacter(scene["主角"], num_maincharacters)
        for i in range(0, num_maincharacters):
            match = re.findall(r'主角姓名：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["姓名"] = match[i]
            match = re.findall(r'主角年龄：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["年龄"] = match[i]
            match = re.findall(r'主角外貌：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["外貌"] = match[i]
            match = re.findall(r'主角服装：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["服装"] = match[i]
            match = re.findall(r'主角动作：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["动作"] = match[i]
            match = re.findall(r'主角表情：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["表情"] = match[i]
            match = re.findall(r'主角体型：(.*?)\n', input_string)
            if len(match) > 0:
                scene["主角"][i]["体型"] = match[i]
        matches = re.findall(r'配角姓名：', input_string)
        num_supportingroles = len(matches)
        createCharacter(scene["配角"], num_supportingroles)
        for i in range(0, num_supportingroles):
            match = re.findall(r'配角姓名：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["姓名"] = match[i]
            match = re.findall(r'配角年龄：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["年龄"] = match[i]
            match = re.findall(r'配角外貌：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["外貌"] = match[i]
            match = re.findall(r'配角服装：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["服装"] = match[i]
            match = re.findall(r'配角动作：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["动作"] = match[i]
            match = re.findall(r'配角表情：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["表情"] = match[i]
            match = re.findall(r'配角体型：(.*?)\n', input_string)
            if len(match) > 0:
                scene["配角"][i]["体型"] = match[i]
        matches = re.findall(r'名称：', input_string)
        num_items = len(matches)
        createItem(scene["重要物品"], num_items)
        for i in range(0, num_items):
            match = re.findall(r'名称：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["名称"] = match[i]
            match = re.findall(r'物品数量：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["数量"] = match[i]
            match = re.findall(r'形状：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["形状"] = match[i]
            match = re.findall(r'颜色：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["颜色"] = match[i]
            match = re.findall(r'物品大小：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["大小"] = match[i]
            match = re.findall(r'特征：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要物品"][i]["特征"] = match[i]
        matches = re.findall(r'种类：', input_string)
        num_animals = len(matches)
        createAnimal(scene["重要动物"], num_animals)
        for i in range(0, num_animals):
            match = re.findall(r'种类：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["种类"] = match[i]
            match = re.findall(r'动物数量：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["数量"] = match[i]
            match = re.findall(r'体型：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["体型"] = match[i]
            match = re.findall(r'动作：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["动作"] = match[i]
            match = re.findall(r'动物大小：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["大小"] = match[i]
            match = re.findall(r'外表：(.*?)\n', input_string)
            if len(match) > 0:
                scene["重要动物"][i]["外表"] = match[i]
        match = re.search(r'主角，配角，重要物品，重要动物之间的位置关系：(.*?)\n', input_string)
        scene["位置关系"] = self.completeDict(match)
        scene["场景风格"] = re.search(r'场景风格：(.*?)\n', input_string).group(1)
        scene["主要事件"] = input_string.split("主要事件：")[1]

    def completeDict(self, match):
        scene = ""
        if match:
            scene = match.group(1)
        else:
            scene = ""
        return scene

    def clear(self):
        self.buffer = ""

        self.core_info = []

    # 将所有选段分析为字典形式
    def get_core(self, folder_path, start_index, amount):
        prompt1 = "下面我会给你一系列的文本，选择一个最重要的场景，输出格式如下，若文中没有，可填无：时间：地点：天气：主角（可有多个）{" \
                  "主角姓名：主角外貌（不包括服装和装饰品）：主角年龄：主角服装（包括装饰品）：主角动作：主角表情：主角体型：}配角（可有多个）{" \
                  "配角姓名：配角外貌（不包括服装和装饰品）：配角年龄：配角服装（包括装饰品）：配角动作：配角表情：配角体型：}重要物品（可有多个，不包括主角服装和装饰品）{" \
                  "名称：物品数量：形状：颜色：物品大小：特征：}重要动物（可有多个）{" \
                  "种类：动物数量：动物大小：体型：动作：外表：}主角，配角，重要物品，重要动物之间的位置关系：场景风格：主要事件（只有一个）：\n"
        prompt2 = "继续根据文本选择一个最重要的场景，输出格式如下，若文中没有，可填无：时间：地点：天气：主角（可有多个）{" \
                  "主角姓名：主角外貌（不包括服装和装饰品）：主角年龄：主角服装（包括装饰品）：主角动作：主角表情：主角体型：}配角（可有多个）{" \
                  "配角姓名：配角外貌（不包括服装和装饰品）：配角年龄：配角服装（包括装饰品）：配角动作：配角表情：配角体型：}重要物品（可有多个，不包括主角服装和装饰品）{" \
                  "名称：物品数量：形状：颜色：物品大小：特征：}重要动物（可有多个）{" \
                  "种类：动物数量：动物大小：体型：动作：外表：}主角，配角，重要物品，重要动物之间的位置关系：场景风格：主要事件（只有一个）：\n"
        for i in range(start_index, start_index + amount):
            with open(folder_path + f"/{i}.txt", encoding="utf-8") as segment:
                content = segment.read()
                response = self.get_answer((prompt1 if i == 0 else prompt2) + content)
                self.core_info.append(response)

    # indexs是储存的重要段落的index_list,folderName储存的是切分好的小说段落,将所有选段分析为字典后,将index选择的段落放入dic输出,这是为了保证一致性
    def getIndexDictionary(self, indexs, folderName, DefaultTextAmount=10):  # 此方法用于外部直接调用,直接得到所需字典
        file_sum = count_files_in_folder(folderName)
        self.createDictionary(file_sum)
        num = 0
        for i in range(0, int(file_sum / 10) + 1):
            self.get_core(folderName, i * 10 + 1, DefaultTextAmount if (file_sum >= DefaultTextAmount) else file_sum)
            for j in range(0, DefaultTextAmount if (file_sum >= DefaultTextAmount) else file_sum):
                self.completeDictionary(self.core_info[j], self.scenes[num])
                num = num + 1
            file_sum -= DefaultTextAmount
            self.clear()
        dictionarys = []
        for i in range(0, len(indexs)):
            dictionarys.append(self.scenes[indexs[i]])
        return dictionarys


if __name__ == '__main__':
    processor = TextToDictionary()
    processor.getIndexDictionary([0], "社戏_segments")
