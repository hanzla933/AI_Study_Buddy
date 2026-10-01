from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pypdf.errors import PdfReadError

from app.pdf_reader import extract_text_from_pdf

PROJECT_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_DIR / "static"

app = FastAPI(title="AI Study Buddy")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/documents/extract")
async def extract_document(file: UploadFile = File(...)) -> dict[str, str]:
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Please upload a PDF file.")

    pdf_bytes = await file.read()
    try:
        text = extract_text_from_pdf(pdf_bytes)
    except PdfReadError as error:
        raise HTTPException(status_code=400, detail="The uploaded PDF could not be read.") from error
    finally:
        await file.close()

    return {"filename": file.filename, "text": text}