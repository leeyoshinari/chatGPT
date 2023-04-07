# ChatGPT ![](https://visitor-badge.glitch.me/badge?page_id=leeyoshinari)
一个比较简洁好用的GPT客户端。调用官方API

## 功能
- [x] 像官方客户端那样支持实时显示回答
- [x] 重试对话，让ChatGPT再回答一次
- [x] 无限长度对话
- [x] 从互联网搜索结果
- [x] 将大段代码显示在代码块中

## 部署
1. **下载本项目**

	```shell
	git clone https://github.com/leeyoshinari/chatGPT.git
	cd chatGPT
	```

2. **填写API密钥**

	在`utils.py`中第29行填写你的API密钥

3. **启动**

	```shell
	python3 chatGPT.py
	```

如果一切顺利，现在，你应该已经可以在浏览器地址栏中输入 [`http://localhost:7860`](http://localhost:7860) 查看并使用 ChatGPT 了。

鸣谢 [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)
