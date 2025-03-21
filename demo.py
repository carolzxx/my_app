import gradio as gr

def process_text(text):
    """Convert text to uppercase and count words."""
    uppercase_text = text.upper()
    word_count = len(text.split())
    return uppercase_text, f"Word Count: {word_count}"

with gr.Blocks() as demo:
    gr.Markdown("# 📝 Simple Gradio App (v5.10)")
    gr.Markdown("Enter text below to get the uppercase version and word count.")

    with gr.Row():
        input_text = gr.Textbox(label="Enter Text", placeholder="Type here...")
    
    with gr.Row():
        output_text = gr.Textbox(label="Uppercase Output", interactive=False)
        word_count = gr.Textbox(label="Word Count", interactive=False)

    submit_button = gr.Button("Process")

    submit_button.click(process_text, inputs=input_text, outputs=[output_text, word_count])

if __name__ == "__main__":
    demo.launch()
