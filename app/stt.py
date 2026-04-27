from groq import Groq
import os
from app.config import GROQ_API_KEY

groq_client = Groq(api_key=GROQ_API_KEY)

async def transcribe_audio(audio_file_path: str, file_extension: str):
    """
    Transcribe audio using Groq's Whisper model
    
    Args:
        audio_file_path: Path to the temporary audio file
        file_extension: Extension of the audio file (.mp3, .webm, etc.)
    """
    try:
        # Open the file in binary mode
        with open(audio_file_path, 'rb') as audio_file:
            # 1. Transcribe speech (original language)
            res = groq_client.audio.transcriptions.create(
                file=(f"audio.{file_extension}", audio_file.read()),
                model="whisper-large-v3-turbo"
            )
            original_text = res.text
        
        # Reopen file for language detection
        with open(audio_file_path, 'rb') as audio_file:
            # 2. Detect language using verbose_json
            lang_res = groq_client.audio.transcriptions.create(
                file=(f"audio.{file_extension}", audio_file.read()),
                model="whisper-large-v3-turbo",
                response_format="verbose_json"
            )
            detected_lang = lang_res.language
        
        return original_text, detected_lang
    
    except Exception as e:
        raise Exception(f"Transcription failed: {str(e)}")