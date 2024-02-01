import os
from con1 import Con


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
            if index != -1 & index >= 500:
                self.buffer = segment[index + 1: len(segment)]
            with open(segment_file_path, 'w', encoding=encoding) as segment_file:
                segment_file.write(segment)
        return folder_name

    def get_core(self, folder_path, start_index, amount):
        prompt1 = "下面我会给你一系列的文本，你要分别从里面提取出最重要的情节，并给我不超过50字的概括,回答格式为直接输出概括内容\n"
        prompt2 = "下面继续给我50字以内的概括，回答格式为直接输出概括内容：\n"
        for i in range(start_index, start_index + amount):
            with open(folder_path + f"/{i}.txt", encoding="utf-8") as segment:
                content = segment.read()
                response = self.get_answer((prompt1 if i == 0 else prompt2) + content)
                self.core_info.append(response)

    def get_core_index(self):
        plots = ""
        index = 0
        for plot in self.core_info:
            plots += f"{index}.{plot}\n"
        prompt = "从以下情节概括描述里挑出最重要的一个，告诉我索引，即我标注的序号,回答格式为仅回答一个数字。\n" + plots
        response = self.get_answer(prompt)
        return int(response)

    def clear(self):
        self.buffer = ""
        self.core_info = []

    def get_index(self, text_path, encoding="utf-8"):  # 此方法用于外部直接调用
        DefaultTextAmount = 10
        indexes = []
        folder_name = self.cut_text(text_path, encoding)
        file_sum = count_files_in_folder(folder_name)
        for i in range(0, int(file_sum / 10) + 1):
            self.get_core(folder_name, i * 10 + 1, DefaultTextAmount if (file_sum >= DefaultTextAmount) else file_sum)
            file_sum -= DefaultTextAmount
            index = self.get_core_index()
            self.clear()
            indexes.append(index + i * 10)
        return indexes


if __name__ == '__main__':
    processor = TextProcessor()
    processor.get_index(text_path="novels/警察与赞美诗.txt")
