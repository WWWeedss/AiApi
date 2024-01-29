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