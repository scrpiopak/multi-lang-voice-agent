from groq import Groq
from app.config import GROQ_API_KEY

groq_client = Groq(api_key=GROQ_API_KEY)

async def run_llm(text_en: str):
    try:
        res = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You must think and respond in English only. Keep responses concise and helpful."},
                {"role": "user", "content": text_en}
            ],
            temperature=1,
            max_completion_tokens=150
        )
        return res.choices[0].message.content  # Fixed: use .content instead of ["content"]
    
    except Exception as e:
        raise Exception(f"LLM processing failed: {str(e)}")
    