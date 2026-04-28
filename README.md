PROJECT INFO. & REQUIREMENTS

(1) In main.py set RUN_LOCALLY = True

(2) In index.html use this const response = await fetch('http://127.0.0.1:8000/voice', {

(3) static / index.html has GUI code and run in browser, run both GUI frontend and backend and start recording message

(4) app / -- it is banckend application 
    main.py -> receive/send voice message from GUI frontend
    sst.py -> convert from speech to text
    translate.py -> translate text into english from any language and again from english to any language 
    llm.py -> answer the query in english
    tts.py -> convert text to speech

(5) GROQ is used for this complete pipe line, use your GROQ API KEY

(6) Package requirements
    python = 3.11 
    fastapi>=0.136.1 
    groq>=1.2.0 
    python-dotenv>=1.2.2 
    python-multipart>=0.0.26 
    uvicorn>=0.46.0

(7) vs code and uv is used for this project 
    uv init voice-agent 
    cd voice-agent 
    uv add fastapi uvicorn python-dotenv groq 
    uv run uvicorn app.main:app --reload --port 8000

FOR RAILWAY DEPLOYMENT

(1) In main.py set RUN_LOCALLY = False

(2) In index.html use this const response = await fetch('https://voice-agent-production.up.railway.app/voice', {

    // here give actual address which Railway will give you.

(3) upload index.html to any web hosting server (www.pakistanpipes.com)

(4) generate requirements.txt with uv pip freeze > requirements.txt

(5) Create Procfile with no extension having followin code to tell Railway exactly how to run your FastAPI app.
    web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

(6) Now go to https://railway.app login with GitHub

(7) New Project → Deploy from GitHub Select scrpiopak/multi-lang-voice-agent

(8) Add environment variables 
    GROQ_API_KEY = your_key
    PYTHON_VERSION = 3.11

(9) Now check ur backend running or not at https://web-production-378bf.up.railway.app/docs (address provided by railway)    

(10) Now backend running on Railway with above address and we have to change this in our index.html fetch("https://web-production-378bf.up.railway.app/voice")

(11) Deploy your index.html to https://www.pakistanpipes.com/voice/index.html

(12) Now frontend on www.pakistanpipes.com and backend on Railway

(13) ENJOY !!!