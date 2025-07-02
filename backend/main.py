from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response 
import fitz  # PyMuPDF
import re
from llm import process_file

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://jar-notes-h6xy.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend running ✅"}



@app.options("/upload")
async def options_upload():
    return Response(status_code=204)


@app.post("/upload")
async def upload_file(
    upload_doc: UploadFile = File(...),
    task: str = Form(...),
    keyword: str = Form(default="")
):
    try:
        if not upload_doc.filename.endswith(".pdf"):
            return JSONResponse(status_code=400, content={"error": "Only PDF files supported."})

        pdf_bytes = await upload_doc.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = "".join([page.get_text() for page in doc])
        doc.close()

        result = process_file(text, task, keyword)
        cleaned = re.sub(r'[*#`_~]+', '', result)

        return JSONResponse(content={
            "filename": upload_doc.filename,
            "task": task,
            "keyword": keyword,
            "result_from_jarvis": cleaned
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
