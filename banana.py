import os
from google import genai

def get_banana():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)