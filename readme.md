前置准备：
1.请获取key后添加用户环境变量
"OPENAI_API_KEY"="YOUR-KEY"
并重启IDE

2.使用API需要科学上网

3.https://platform.openai.com/account/limits 查询目前可用模型

目前的实现：

1.gpt3.5有上下文的文本To文本，可以使用中文,函数参数详情见con1.py文件
请在gpt.py中使用相应的函数，输入字符串返回字符串

2.不支持上下文的文生图,输入prompt返回url字符串，有其他不可见参数可自主修改，
建议不要修改生成数量，测试生成多张图片仅生成多张一样的图片，支持dall-e-3和
dalle-e-2,url将会在一小时内过期，请及时保存图片

3.部分重绘(仅支持dall-e-2模型)，提供原始图片url和蒙版的url，prompt，只
修改蒙版透明区域对应的原始图，获得一个url，详情请参考：
https://platform.openai.com/docs/guides/images/usage?context=node
未尝试能否替代图生图，有待考证。

4.assistant api,无限长度的上下文，支持添加文件并分析文件。模型暂时只支持
gpt-3.5-turbo-1106
详细调用顺序为：

create_assistant()创建助手，

open_file()上传文件获取文件id,

add_assistant_file()和add_assistant()添加要求/文件,

run_assistant()运行进程,robot进行一次检测和输出

show_message()显示运行结果

注：(1)现在的模式一次只维护一个assistant，一个thread，一个run，有并行需求
可以日后修改。

(2)使用者需要自己维护file_ids这个list。

(3)在已经创建了一个run进程之后，在这个run进程结束之前你无法进行add操作，
为了确保已经结束，你可以手动show_message(),show_message()有确保当前run
进程结束的功能。

(4)使用open_file函数会让该文件被上传到服务器，因此记录下file_id后可以不再
调用open_file函数

5.关于fine-tune模型问题:

(1)需要升级到付费用户

(2)没搞懂validation data是干啥的

(3)训练数据格式参考tune.jsonl文件

(4)微调模型会存储在openai服务器内

https://platform.openai.com/finetune


关于ErnieApi.py中的文心一言api
调用方式与