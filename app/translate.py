# from openai import OpenAI
from groq import Groq
from app.config import GROQ_API_KEY

groq_client = Groq(api_key=GROQ_API_KEY)

async def translate_text(text: str, target_lang: str):
    try:
        res = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"Translate the following text into {target_lang}. Only output the translated text, nothing else."},
                {"role": "user", "content": text}
            ]
        )
        return res.choices[0].message.content
    
    except Exception as e:
        # If translation fails, return original text
        print(f"Translation error: {e}")
        return text