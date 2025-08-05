import os
from dotenv import load_dotenv
from groq import Groq
from reflection_pattern.reflection_agent import ReflectionAgent

load_dotenv()

# Create reflection agent
model1="meta-llama/llama-4-scout-17b-16e-instruct"
model2="llama3-70b-8192"
model3='gemma2-9b-it'
agent = ReflectionAgent(model=model3)

def generate_drydock_specification(user_input):
    prompt = f"""
    Generate a professional drydock specification in Word-compatible HTML for:
    {user_input}

    ### FORMAT GUIDELINES ###
    - Title: <div class="main-title">REPAIR SPECIFICATION: {user_input.upper()}</div>
    - Sections:
        1. DESCRIPTION
        2. SCOPE OF WORK / INSTRUCTIONS (includes Preparatory Measures, Job Breakdown, Safety Controls, Standards & Compliance, Documentation)
        3. MATERIAL & SUPPORT
        4. SERVICE LINES (must be a bordered table)
        5. APPROVALS & SUPERVISION
    - Use span tags with class="placeholder" for placeholders like [MAKE], [MODEL], [LOCATION]
    - Font: 'Poppins', font-size: 14px, line-height: 1.6
    - Use <ul>, <ol>, and <table> appropriately
    - Include class="safety-box" for Safety Controls section
    - Output HTML body content only (without <html> or <head> tags)
    """

    output = agent.run(
        user_msg=prompt,
        generation_system_prompt="You are a marine technical writer creating structured, class-compliant drydock specification HTML documents for Word.",
        reflection_system_prompt="You are a ship superintendent reviewing HTML drydock specifications. Ensure all 5 required sections are present, formatted correctly, and styled with placeholders and classes (like 'main-title', 'placeholder', 'safety-box', and table structure). If formatting or content deviates, fix it.",
        n_steps=2,
        verbose=1
    )

    safe_filename = user_input.replace(" ", "_").replace("/", "_").replace("\\", "_")

    html_template = f"""
    <!DOCTYPE html>
    <html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta charset="UTF-8">
      <meta name="ProgId" content="Word.Document">
      <meta name="Generator" content="Microsoft Word">
      <meta name="Originator" content="Microsoft Word">
      <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
      <style>
        body {{ font-family: 'Poppins', sans-serif; font-size: 14px; line-height: 1.6; margin: 20px; }}
        .main-title {{ font-size: 16px; font-weight: bold; text-transform: uppercase; margin-bottom: 20px; }}
        .section-header {{ background-color: #000; color: #fff; font-weight: bold; padding: 8px 12px; margin: 20px 0 10px 0; text-transform: uppercase; }}
        .placeholder {{ background-color: #e3f2fd; color: #0d47a1; font-weight: 600; padding: 2px 4px; }}
        .subsection-title {{ font-weight: 700; margin: 10px 0 5px 0; }}
        .safety-box {{ background-color: #fff3cd !important; border: 2px solid #ffeaa7; padding: 15px; margin: 15px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; }}
        th, td {{ border: 1px solid #000; padding: 8px; text-align: left; vertical-align: top; }}
        th {{ background-color: #f8f9fa; font-weight: 700; text-align: center; }}
      </style>
    </head>
    <body>
      <div class="main-title">REPAIR SPECIFICATION: {user_input.upper()}</div>
      {output}
    </body>
    </html>
    """

    os.makedirs("html_pages", exist_ok=True)
    with open(f"html_pages/{safe_filename}_drydock_specification.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✅ Saved: html_pages/{safe_filename}_drydock_specification.html")
