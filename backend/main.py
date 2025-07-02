from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import fitz  # PyMuPDF
import re
from backend.llm import process_file


app = FastAPI()


templates = Jinja2Templates(directory="backend/jinja2templates")



@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(
    upload_doc: UploadFile = File(...),
    task: str = Form(...),
    keyword: str = Form(default="")
):
    try:
        # Validate file type
        if not upload_doc.filename or not upload_doc.filename.lower().endswith(".pdf"):
            return JSONResponse(
                status_code=400, 
                content={"error": "Only PDF files are supported."}
            )

        # Read and process PDF
        pdf_bytes = await upload_doc.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "".join([page.get_text() for page in doc])
        doc.close()

        # Process with your LLM function
        result = process_file(text, task, keyword)
        cleaned = re.sub(r'[*#`_~]+', '', result)

        return JSONResponse(
            content={
                "filename": upload_doc.filename,
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

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Server is running"}
