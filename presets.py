# -*- coding:utf-8 -*-
title = """<h1 align="left" style="min-width:200px; margin-top:0;">ChatGPT</h1>"""
description = """<div align="center" style="margin:16px 0">
</div>
"""
customCSS = """
#status_display {
    display: flex;
    min-height: 2.5em;
    align-items: flex-end;
    justify-content: flex-end;
}
#status_display p {
    font-size: .85em;
    font-family: monospace;
    color: var(--text-color-subdued) !important;
}
[class *= "message"] {
    border-radius: var(--radius-xl) !important;
    border: none;
    padding: var(--spacing-xl) !important;
    font-size: var(--text-md) !important;
    line-height: var(--line-md) !important;
}
[data-testid = "bot"] {
    max-width: 85%;
    border-bottom-left-radius: 0 !important;
}
[data-testid = "user"] {
    max-width: 85%;
    width: auto !important;
    border-bottom-right-radius: 0 !important;
}
code {
    display: inline;
    white-space: break-spaces;
    border-radius: 6px;
    margin: 0 2px 0 2px;
    padding: .2em .4em .1em .4em;
    background-color: rgba(175,184,193,0.2);
}
pre code {
    display: block;
    white-space: pre;
    background-color: hsla(0, 0%, 0%, 72%);
    border: solid 5px var(--color-border-primary) !important;
    border-radius: 10px;
    padding: 0 1.2rem 1.2rem;
    margin-top: 1em !important;
    color: #FFF;
    box-shadow: inset 0px 8px 16px hsla(0, 0%, 0%, .2)
}

* {
    transition: all 0.6s;
}
"""

summarize_prompt = "你是谁？我们刚才聊了什么？" # 总结对话时的 prompt
MODELS = ["gpt-3.5-turbo"] #"gpt-3.5-turbo", "gpt-3.5-turbo-0301", "gpt-4","gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314" # 可选的模型
# act_prompts = json.load(open('./templates/Prompts.json', 'r', encoding='utf-8'))
websearch_prompt = """Web search results:

{web_results}
Current date: {current_date}

Instructions: Using the provided web search results, write a comprehensive reply to the given query. Make sure to cite results using [[number](URL)] notation after the reference. If the provided search results refer to multiple subjects with the same name, write separate answers for each subject.
Query: {query}
Reply in 中文"""

# 错误信息
standard_error_msg = "☹️发生了错误：" # 错误信息的标准前缀
error_retrieve_prompt = "请检查网络连接，或者API-Key是否有效。" # 获取对话时发生错误
connection_timeout_prompt = "连接超时，无法获取对话。" # 连接超时
read_timeout_prompt = "读取超时，无法获取对话。" # 读取超时
proxy_error_prompt = "代理错误，无法获取对话。" # 代理错误
ssl_error_prompt = "SSL错误，无法获取对话。" # SSL 错误
no_apikey_msg = "API key长度不是51位，请检查是否输入正确。" # API key 长度不足 51 位

max_token_streaming = 3500 # 流式对话时的最大 token 数
timeout_streaming = 60 # 流式对话时的超时时间
max_token_all = 3500 # 非流式对话时的最大 token 数
timeout_all = 200 # 非流式对话时的超时时间
enable_streaming_option = True  # 是否启用选择选择是否实时显示回答的勾选框
HIDE_MY_KEY = False # 如果你想在UI中隐藏你的 API 密钥，将此值设置为 True
