from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from llm import process_file
import fitz  # PyMuPDF
import re

app = FastAPI()

# ✅ Proper CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://jar-notes-h6xy.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="jinja2Templates")

@app.get("/")
def home():
    return {"message": "Welcome to JarNotes! the Backend is running."}

@app.post("/upload")
async def upload_file(
    upload_doc: UploadFile = File(...),
    task: str = Form(...),
    keyword: str = Form(default="")
):
    try:
        if upload_doc.filename.endswith(".pdf"):
            pdf_bytes = await upload_doc.read()
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            text = "".join([page.get_text() for page in doc])
            doc.close()

            result = process_file(text, task, keyword)
            cleaned_result = re.sub(r'[*#`_~]+', '', result)

            return JSONResponse(content={
                "filename": upload_doc.filename,
                "content_type": upload_doc.content_type,
                "task": task,
                "keyword": keyword,
                "result_from_jarvis": cleaned_result
            })
        else:
            return JSONResponse(status_code=400, content={"error": "Only PDF files are supported."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
