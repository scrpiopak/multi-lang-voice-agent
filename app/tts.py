import base64
from groq import Groq
from app.config import GROQ_API_KEY

groq_client = Groq(api_key=GROQ_API_KEY)

async def synthesize_speech(text: str):
    try:
        response  = groq_client.audio.speech.create(
            model="canopylabs/orpheus-v1-english",
            voice="autumn",
            response_format="wav",
            input=text
        )
        # Extract raw audio bytes
        audio_bytes = response.read()

        # Convert to base64 for frontend
        return base64.b64encode(audio_bytes).decode("utf-8")    
    
    except Exception as e:
        raise Exception(f"TTS synthesis failed: {str(e)}")