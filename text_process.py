import os
from con1 import Con

gpt = Con("gpt-3.5-turbo", "a text analysis assistant")

path = "novels/变色龙.txt"


# prompt = "对以下小说文本进行分析，以中文的json格式回答我，包含主人公、场景、配角、小说情感基调、重要情节段落：\n"


def count_files_in_folder(folder_path):
    file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
    return file_count


class TextProcessor:
    buffer = ""
    core_info = []
    gpt = Con("gpt-3.5-turbo", "a text analysis assistant")

    def get_answer(self, prompt):
        response = self.gpt.textToText(prompt)
        return response

    def cut_text(self, text_path, encoding):
        with open(text_path, 'r', encoding=encoding) as text:
            content = text.read()
        segments = [content[i:i + 1000] for i in range(0, len(content), 1000)]

        # 创建存放段落的文件夹
        folder_name = os.path.splitext(os.path.basename(text_path))[0] + "_segments"
        os.makedirs(folder_name, exist_ok=True)

        # 将分割后的内容写入小文件中
        for i, segment in enumerate(segments):
            segment_file_path = os.path.join(folder_name, f"{i + 1}.txt")
            if self.buffer != "":
                segment = self.buffer + segment
                self.buffer = ""
            index = segment.rfind('\n')
            if index != -1:
                self.buffer = segment[index + 1: len(segment)]
            with open(segment_file_path, 'w', encoding=encoding) as segment_file:
                segment_file.write(segment)

    def get_core(self, folder_path):
        count = self.count_files_in_folder(folder_path)
        for i in range(0, count):
            with open(folder_path + f"/{i}.txt") as segment:
                content = segment.read()
                response = self.get_answer((i == 0 if "下面我会给你一系列的文本，你要分别从里面提取出最重要的情节，并给我不超过50字的概括,回答格式为直接输出概括内容\n"
                                            else "下面继续给我50字以内的概括，回答格式为直接输出概括内容：\n") + content)
                self.core_info.append(response)
        return self.core_info

    def get_core_index(self):
        plots = ""
        index = 0
        for plot in self.core_info:
            plots += f"{index}.{plot}\n"
        prompt = "从以下情节概括描述里挑出最重要的一个，告诉我索引，即我标注的序号,回答格式为仅回答一个数字。\n" + plots
        response = self.get_answer(prompt)
        return int(response)


if __name__ == '__main__':
    cut_text("novels/警察与赞美诗.txt", "utf-8")
    print(count_files_in_folder("novels"))
