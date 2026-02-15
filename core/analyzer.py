# core/analyzer.py

import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME


# ---------------------------------------------------
# Configure Gemini
# ---------------------------------------------------
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    raise Exception(f"Gemini configuration failed: {e}")


# ---------------------------------------------------
# Main Resume Analysis Function
# ---------------------------------------------------
def analyze_resume(resume_text: str) -> str:
    """
    Sends resume text to Gemini and returns
    short, line-by-line improvement suggestions.
    """

    if not resume_text.strip():
        return "Resume text is empty. Please upload a valid file."

    prompt = f"""
You are an expert resume reviewer.

Your task:
- Analyze the resume line by line.
- Identify only weak or unclear lines.
- Suggest a stronger version.
- Keep suggestions SHORT (max 1–2 lines).
- Do NOT give long explanations.
- Do NOT rewrite the entire resume.
- Do NOT add unnecessary commentary.

Strict Output Format:

Weak Line:
<original weak sentence>

Improved Version:
<better version>

Resume:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)

        if not response or not response.text:
            return "AI returned an empty response."

        return response.text.strip()

    except Exception as e:
        return f"Error during AI analysis: {str(e)}"
