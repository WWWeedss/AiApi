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
建议不要修改生成数量，测试生成多张图片仅生成多张一样的图片
