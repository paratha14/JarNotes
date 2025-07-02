from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response 
import fitz  # PyMuPDF
import re
from llm import process_file

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://jar-notes-h6xy.vercel.app",
        "https://jar-notes-h6xy-k9zzhjv03-paratha14s-projects.vercel.app",  
        "http://localhost:3000",  
        "http://127.0.0.1:3000"  
    ],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "PUT", "DELETE"],  
    allow_headers=[
        "Accept",
        "Accept-Language", 
        "Content-Language",
        "Content-Type",
        "Authorization",
        "X-Requested-With",
        "Origin",
        "Access-Control-Request-Method",
        "Access-Control-Request-Headers"
    ],
    expose_headers=["*"],
    max_age=86400  
)

@app.get("/")
def read_root():
    return {"message": "Backend running ✅"}


@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "https://jar-notes-h6xy.vercel.app",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, DELETE",
            "Access-Control-Allow-Headers": "Accept, Accept-Language, Content-Language, Content-Type, Authorization, X-Requested-With, Origin, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": "86400"
        }
    )

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
                content={"error": "Only PDF files are supported."},
                headers={
                    "Access-Control-Allow-Origin": "https://jar-notes-h6xy.vercel.app",
                    "Access-Control-Allow-Credentials": "true"
                }
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
            },
            headers={
                "Access-Control-Allow-Origin": "https://jar-notes-h6xy.vercel.app",
                "Access-Control-Allow-Credentials": "true"
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)},
            headers={
                "Access-Control-Allow-Origin": "https://jar-notes-h6xy.vercel.app",
                "Access-Control-Allow-Credentials": "true"
            }
        )

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Server is running"}

