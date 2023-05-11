import gradio as gr


def hello(i):
    # classifier = pipeline("sentiment-analysis")
    # a = classifier(i)
    # return a
    a = 1/0
    return "hello world!"
a = 1/0
iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0")
