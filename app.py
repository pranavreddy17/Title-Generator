import gradio as gr
from transformers import pipeline

# Load summarization pipeline (or any model you like)
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_metadata(script):
    # Use prompt engineering to get metadata
    prompt = f"Generate a YouTube title and description for this script:\n{script}"
    result = generator(prompt, max_new_tokens=100)[0]["generated_text"]

    # Simple parsing (you can improve this!)
    if "\n" in result:
        title, description = result.split("\n", 1)
    else:
        title = result
        description = "No description found."

    return title.strip(), description.strip()

iface = gr.Interface(
    fn=generate_metadata,
    inputs=gr.Textbox(lines=10, label="YouTube Video Script"),
    outputs=[
        gr.Textbox(label="Title"),
        gr.Textbox(label="Description")
    ],
    title="🎬 YouTube Metadata Generator",
    description="Free YouTube Title & Description generator using Hugging Face transformers."
)

if __name__ == "__main__":
    iface.launch()
