import gradio as gr
from session import QuizSession
from ui_helpers import q_html, r_html

session = QuizSession()

def generate(file):
    session.load_document(file.name, 5)
    q = session.current_question()
    return q_html(q, 1, 5)

def submit(ans):
    r = session.submit_answer(ans)
    return r_html(r)

with gr.Blocks() as app:
    file = gr.File()
    btn = gr.Button("Generate")
    out = gr.HTML()

    ans = gr.Textbox()
    submit_btn = gr.Button("Submit")
    res = gr.HTML()

    btn.click(generate, inputs=file, outputs=out)
    submit_btn.click(submit, inputs=ans, outputs=res)

app.launch()
