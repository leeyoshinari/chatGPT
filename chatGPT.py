# -*- coding:utf-8 -*-
from utils import *
from presets import *

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")

gr.Chatbot.postprocess = postprocess

with gr.Blocks(css=customCSS) as demo:
    history = gr.State([])
    token_count = gr.State([])

    with gr.Row():
        gr.HTML(title)
        status_display = gr.Markdown("status: ready", elem_id="status_display")

    with gr.Row(scale=1).style(equal_height=True):
        with gr.Column(scale=5):
            with gr.Row(scale=1):
                chatbot = gr.Chatbot().style(height=800)  # .style(color_map=("#1D51EE", "#585A5B"))
            with gr.Row(scale=1):
                with gr.Column(scale=12):
                    user_input = gr.Textbox(show_label=False, placeholder="在这里输入").style(
                        container=False)
                with gr.Column(min_width=50, scale=1):
                    submitBtn = gr.Button("🚀", variant="primary")
            with gr.Row(scale=1):
                emptyBtn = gr.Button("🧹 新的对话",)
                retryBtn = gr.Button("🔄 重新生成")
                reduceTokenBtn = gr.Button("♻️ 总结对话")

        with gr.Column():
            with gr.Column(min_width=50,scale=1):
                with gr.Tab(label="设置"):
                    model_select_dropdown = gr.Dropdown(label="选择模型", choices=MODELS, multiselect=False, value=MODELS[0])
                    # act_prompts_select_dropdown = gr.Dropdown(label="行为提示", choices=act_prompts, multiselect=False, value=act_prompts[0])
                    with gr.Accordion("参数", open=False):
                        top_p = gr.Slider(minimum=-0, maximum=1.0, value=1.0, step=0.05,
                                        interactive=True, label="Top-p (nucleus sampling)",)
                        temperature = gr.Slider(minimum=-0, maximum=2.0, value=1.0,
                                                step=0.1, interactive=True, label="Temperature",)
                    use_streaming_checkbox = gr.Checkbox(label="实时传输回答", value=True, visible=enable_streaming_option)
                    use_websearch_checkbox = gr.Checkbox(label="使用在线搜索", value=False)

    gr.Markdown(description)

    user_input.submit(predict, [history, user_input, chatbot, token_count, top_p, temperature, use_streaming_checkbox, model_select_dropdown, use_websearch_checkbox], [chatbot, history, status_display, token_count], show_progress=True)
    user_input.submit(reset_textbox, [], [user_input])

    submitBtn.click(predict, [history, user_input, chatbot, token_count, top_p, temperature, use_streaming_checkbox, model_select_dropdown, use_websearch_checkbox], [chatbot, history, status_display, token_count], show_progress=True)
    submitBtn.click(reset_textbox, [], [user_input])

    emptyBtn.click(reset_state, outputs=[chatbot, history, token_count, status_display], show_progress=True)

    retryBtn.click(retry, [history, chatbot, token_count, top_p, temperature, use_streaming_checkbox, model_select_dropdown], [chatbot, history, status_display, token_count], show_progress=True)

    reduceTokenBtn.click(reduce_token_size, [history, chatbot, token_count, top_p, temperature, use_streaming_checkbox, model_select_dropdown], [chatbot, history, status_display, token_count], show_progress=True)
    # act_prompts_select_dropdown.change(reset_state, [act_prompts_select_dropdown], [], show_progress=True)

logging.info(colorama.Back.GREEN + "\n访问 http://localhost:7860 查看界面" + colorama.Style.RESET_ALL)
# 默认开启本地服务器，默认可以直接从IP访问，默认不创建公开分享链接
demo.title = "ChatGPT"

if __name__ == "__main__":
    # demo.queue().launch(share=False) # 改为 share=True 可以创建公开分享链接
    demo.queue().launch(server_name="0.0.0.0", server_port=7860, share=False) # 可自定义端口
    #demo.queue().launch(server_name="0.0.0.0", server_port=7860,auth=("在这里填写用户名", "在这里填写密码")) # 可设置用户名与密码
    #demo.queue().launch(auth=("在这里填写用户名", "在这里填写密码")) # 适合Nginx反向代理
