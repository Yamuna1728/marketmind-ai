import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Gemini Key Loaded:", bool(api_key))

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

def generate_content(prompt: str):
    try:
        print("Sending request to Gemini...")

        response = model.generate_content(prompt)

        print("Gemini responded successfully")

        return response.text

    except Exception as e:
        print("GEMINI ERROR:")
        print(str(e))
        raise e