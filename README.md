PROJECT INFO. & REQUIREMENTS

(1) static / index.html has GUI code and run in browser, run both GUI frontend and backend and start recording message

(2) app / -- it is banckend application 
    main.py -> receive/send voice message from GUI frontend
    sst.py -> convert from speech to text
    translate.py -> translate text into english from any language and again from english to any language 
    llm.py -> answer the query in english
    tts.py -> convert text to speech

(3) GROQ is used for this complete pipe line, use your GROQ API KEY

(4) Package requirements
    python = 3.11 
    fastapi>=0.136.1 
    groq>=1.2.0 
    python-dotenv>=1.2.2 
    python-multipart>=0.0.26 
    uvicorn>=0.46.0

(5) vs code and uv is used for this project 
    uv init voice-agent 
    cd voice-agent 
    uv add fastapi uvicorn python-dotenv groq 
    uv run uvicorn app.main:app --reload --port 8000