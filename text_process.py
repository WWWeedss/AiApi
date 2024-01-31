import os
import con1

gpt = con1.Con("gpt-3.5-turbo", "a text analysis assistant")

path = "novels/变色龙.txt"
buffer = ""

# prompt = "对以下小说文本进行分析，以中文的json格式回答我，包含主人公、场景、配角、小说情感基调、重要情节段落：\n"


def analyse(content):
    prompt = ""  # TODO
    response = gpt.textToText(prompt + content)
    return response


def cut_text(text_path, encoding):
    with open(text_path, 'r', encoding=encoding) as text:
        content = text.read()
    segments = [content[i:i + 1000] for i in range(0, len(content), 1000)]

    # 创建存放段落的文件夹
    folder_name = os.path.splitext(os.path.basename(text_path))[0] + "_segments"
    os.makedirs(folder_name, exist_ok=True)

    # 将分割后的内容写入小文件中
    for i, segment in enumerate(segments):
        segment_file_path = os.path.join(folder_name, f"{i + 1}.txt")
        with open(segment_file_path, 'w', encoding=encoding) as segment_file:
            segment_file.write(segment)


def get_core(folder_path):
    file_path = ""
    count = count_files_in_folder(folder_name)
    core_info = []
    for i in range(0, count):
        with open(folder_path + f"/{i}.txt") as segment:
            content = segment.read()
            response = analyse(content)
            core_info.append(response)
    return core_info


def count_files_in_folder(folder_path):
    file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
    return file_count


if __name__ == '__main__':
    cut_text("novels/警察与赞美诗.txt", "utf-8")
    print(count_files_in_folder("novels"))
