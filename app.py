import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def process_text(text):
    return text.upper()

def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"

with gr.Blocks(title="Simple Gradio App") as demo:
    gr.Markdown("# 🚀 Simple Gradio App on Railway")
    gr.Markdown("Welcome! This is a simple multi-functional Gradio app.")
    
    with gr.Tab("Greeter"):
        gr.Markdown("### Greet Someone")
        with gr.Row():
            name_input = gr.Textbox(label="Enter your name", placeholder="John")
            intensity_input = gr.Slider(1, 5, value=1, step=1, label="Excitement Level")
        greet_button = gr.Button("Greet Me!")
        greet_output = gr.Textbox(label="Greeting")
        greet_button.click(greet, inputs=[name_input, intensity_input], outputs=greet_output)
    
    with gr.Tab("Text Processor"):
        gr.Markdown("### Convert Text to Uppercase")
        text_input = gr.Textbox(label="Enter text", placeholder="Type something...")
        text_button = gr.Button("Convert")
        text_output = gr.Textbox(label="Result")
        text_button.click(process_text, inputs=text_input, outputs=text_output)
    
    with gr.Tab("Calculator"):
        gr.Markdown("### Simple Calculator")
        with gr.Row():
            num1 = gr.Number(label="Number 1", value=0)
            num2 = gr.Number(label="Number 2", value=0)
        operation = gr.Radio(["Add", "Subtract", "Multiply", "Divide"], label="Operation", value="Add")
        calc_button = gr.Button("Calculate")
        calc_output = gr.Textbox(label="Result")
        calc_button.click(calculate, inputs=[num1, num2, operation], outputs=calc_output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
