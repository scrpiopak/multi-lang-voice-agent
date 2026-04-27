from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import tempfile

from app.stt import transcribe_audio
from app.translate import translate_text
from app.llm import run_llm
from app.tts import synthesize_speech

app = FastAPI()

# Serve UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.post("/voice")
async def voice_endpoint(audio: UploadFile = File(...)):
    temp_file_path = None
    try:
        # Validate file type
        allowed_types = ['audio/mpeg', 'audio/mp3', 'audio/mp4', 'audio/webm', 'audio/ogg', 'audio/wav']
        if audio.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail=f"Unsupported audio format. Allowed: {allowed_types}")
        
        # Get file extension
        file_extension = audio.filename.split('.')[-1] if audio.filename and '.' in audio.filename else 'webm'
        
        # Save uploaded file to temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as temp_file_obj:
            content = await audio.read()
            if len(content) == 0:
                raise HTTPException(status_code=400, detail="Empty audio file")
            temp_file_obj.write(content)
            temp_file_path = temp_file_obj.name
        
        print(f"Processing audio file: {temp_file_path} ({len(content)} bytes)")
        
        ###################################################

        # MULTI LANGUAGE

        # # 1. Speech-to-Text (Groq Whisper)
        # original_text, detected_lang = await transcribe_audio(temp_file_path, file_extension)
        # print(f"Transcribed: '{original_text}' (Language: {detected_lang})")
        
        # # 2. Translate original → English
        # text_en = await translate_text(original_text, "en")
        # print(f"Translated to English: '{text_en}'")
        
        # # 3. LLM reasoning in English
        # llm_output_en = await run_llm(text_en)
        # print(f"LLM Response: '{llm_output_en}'")
        
        # # 4. Translate English → user language
        # final_text_user_lang = await translate_text(llm_output_en, detected_lang)
        # print(f"Final response in {detected_lang}: '{final_text_user_lang}'")
        
        # # 5. Text-to-Speech (OpenAI TTS)
        # audio_base64 = await synthesize_speech(final_text_user_lang)
        

        ###################################################
        
        # SINGLE ENGLISH LANGUAGE
        
        # 1. Speech-to-Text (Groq Whisper)
        original_text, detected_lang = await transcribe_audio(temp_file_path, file_extension)
        print(f"Transcribed: '{original_text}' (Language: {detected_lang})")
       
        
        # # 2. LLM reasoning in English
        llm_output_en = await run_llm(original_text)
        print(f"LLM Response: '{llm_output_en}'")
     
        # 3. Text-to-Speech (OpenAI TTS)
        audio_base64 = await synthesize_speech(llm_output_en)


        return {
            "text": llm_output_en,
            "audio_base64": audio_base64,
            "detected_language": detected_lang,
            "original_text": original_text
        }
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in voice endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
    
    finally:
        # Clean up temporary file
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)