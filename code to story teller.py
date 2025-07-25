import gradio as gr
import google.generativeai as genai
import os

# === API Configuration ===
# ✅ Use the actual API key directly or read from environment variable
GEMINI_API_KEY = "AIzaSyAWL6HGeNhgDyCTFfl2_hhTGCptnXT0EHM"  # Or use os.getenv("GEMINI_API_KEY")

# ✅ Configure the Gemini API client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Storytelling Function ===
def code_to_story(code, language):
    try:
        prompt = f"""
You are a storyteller who loves explaining code in an engaging and fun way.
Explain the following code as a story in {language}.
Be creative, clear, and preserve the meaning of the code.

Code:
{code}
"""
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "⚠️ No response text received."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# === Gradio UI ===
with gr.Blocks(title="Code Storyteller") as demo:
    gr.Markdown("""
    # 📖 Code Storyteller  
    *Explain code like a story in your chosen language!*  
    Powered by Gemini 1.5 Flash
    """)
    
    with gr.Row():
        code_input = gr.Textbox(
            lines=15, 
            label="Paste your code",
            placeholder="e.g., a Python loop or JavaScript function"
        )
    
    with gr.Row():
        lang_input = gr.Dropdown(
            choices=["English", "Hindi", "Spanish", "French", "German", "Japanese"],
            label="Select Language",
            value="English"
        )
    
    with gr.Row():
        submit_btn = gr.Button("🧙 Explain Code as a Story")
    
    with gr.Row():
        story_output = gr.Textbox(
            lines=12, 
            label="Storytelling Output", 
            interactive=False
        )
    
    submit_btn.click(fn=code_to_story, inputs=[code_input, lang_input], outputs=story_output)

# ✅ Run the app
if __name__ == "__main__":
    demo.launch(share=True)
