from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import JSONResponse, Response

import fitz  # PyMuPDF
import re
from llm import process_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"message": "Welcome to JarNotes API"}

@app.post("/upload")
async def upload_file(
    pdf: UploadFile = File(...),
    task: str = Form(...),
    keyword: str = Form(default="")
):
    try:
        # Validate file type
        if not pdf.filename or not pdf.filename.lower().endswith(".pdf"):
            return JSONResponse(
                status_code=400, 
                content={"error": "Only PDF files are supported."}
            )

        # Read and process PDF
        pdf_bytes = await pdf.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "".join([page.get_text() for page in doc])
        doc.close()

        # Process with your LLM function
        result = process_file(text, task, keyword)
        cleaned = re.sub(r'[*#`_~]+', '', result)

        return JSONResponse(
            content={
                "filename": pdf.filename,
                "task": task,
                "keyword": keyword,
                "result_from_jarvis": cleaned
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )

@app.head("/")
def read_root_head():
    return Response(status_code=200)
