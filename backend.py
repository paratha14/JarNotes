from typing import Union
from fastapi import FastAPI, Request, File, UploadFile, Form
from pydantic import BaseModel
from llm import process_file
from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import fitz
import re

app= FastAPI()
#env = Environment(loader = FileSystemLoader('jinja2Templates'))
templates= Jinja2Templates(directory="jinja2Templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return {"message": "Welcome to JarNotes! the Backend is running."}

@app.get("/upload", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(upload_doc: UploadFile = File(...), task: str = Form(...), keyword: str = Form(default="")):
    if upload_doc.filename.endswith(".pdf"):
        pdf_bytes = await upload_doc.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        result= process_file(text, task, keyword)
        cleaned_result = re.sub(r'[*#`_~]+', '', result)

        return( JSONResponse(content={
            "filename": upload_doc.filename,
            "content_type": upload_doc.content_type,
            #"extracted_text": text[:1000],
            "task": task,
            "keyword": keyword,  
            "result_from_jarvis":cleaned_result
        }))
    

    print(JSONResponse(content={"error": "Only PDF files are supported currently."}))
