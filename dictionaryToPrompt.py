from con1 import Con  # 导入Con类，用于调用API


class DictionaryToPrompt:
    def __init__(self):
        pass

    def format_characters(self, characters):
        formatted_characters = []
        for character in characters:
            formatted_character = f"{character['姓名']}（{character['外貌']}，{character['年龄']}，{character['服装']}，{character['动作']}，{character['表情']}，{character['体型']}）"
            formatted_characters.append(formatted_character)
        return formatted_characters

    def format_items(self, items):
        formatted_items = []
        for item in items:
            formatted_item = f"{item['名称']}（{item['数量']}，{item['形状']}，{item['颜色']}，{item['大小']}，{item['特征']}）"
            formatted_items.append(formatted_item)
        return formatted_items

    def format_animals(self, animals):
        formatted_animals = []
        for animal in animals:
            formatted_animal = f"{animal['种类']}（{animal['数量']}，{animal['大小']}，{animal['体型']}，{animal['动作']}，{animal['外表']}）"
            formatted_animals.append(formatted_animal)
        return formatted_animals

    def format_relations(self, relations):
        formatted_relations = relations.replace("\n", "，")
        return formatted_relations

    # 将原输入格式(字典 list中包括list)转为一段拼接的字符串
    def format_scene(self, scene):
        formatted_scene = f"时间：{scene['时间']}，地点：{scene['地点']}，天气：{scene['天气']}，" \
                          f"主角：{', '.join(self.format_characters(scene['主角']))}，" \
                          f"配角：{', '.join(self.format_characters(scene['配角']))}，" \
                          f"重要物品：{', '.join(self.format_items(scene['重要物品']))}，" \
                          f"重要动物：{', '.join(self.format_animals(scene['重要动物']))}，" \
                          f"主角，配角，重要物品，重要动物之间的位置关系：{self.format_relations(scene['位置关系'])}，" \
                          f"场景风格：{scene['场景风格']}，主要事件：{scene['主要事件']}"
        return formatted_scene

    # input为原始输入的字典格式
    def organize_list_to_natural_language(self, input_prompt):
        # 创建Con实例并初始化
        gpt = Con("gpt-3.5-turbo", "a text analysis assistant")

        # 构建API请求的prompt
        prompt = (f"将场景描述转换为形如：一张（主要事件名词）的图片，（事情发生的时间、环境），（主角一：年龄、外貌、表情/情感态度），（主角二/配角：年龄、外貌、表情/情感态度），（涉及的物品：[外观] [用途] "
                  f"[物品名称]），人物之间的行为自然语言描述。")+input_prompt

        # 调用API获取响应
        response = gpt.textToText(prompt)

        # 返回API响应
        return str(response)


if __name__ == '__main__':
    processor = DictionaryToPrompt()
    # 调用曹金部分的函数获得输入放到scene中
    scene = {}
    # 将字典拼接为一段字符串
    formatted_prompt = processor.format_scene(scene)
    print(formatted_prompt)
    # 调用api将字典形成的字符串转为自然语言
    result_prompt = processor.organize_list_to_natural_language(formatted_prompt)
    print(result_prompt)
