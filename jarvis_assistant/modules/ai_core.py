from google import genai
from config import GEMINI_API_KEY

MODEL = "gemini-3.8-flash"
client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
