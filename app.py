import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Rafa Amin Gallery")
app.mount("/media", StaticFiles(directory=str(UPLOAD_DIR)), name="media")

@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/api/photos")
async def list_photos():
    allowed = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
    photos = sorted(
        (f"/media/{p.name}" for p in UPLOAD_DIR.iterdir()
         if p.is_file() and p.suffix.lower() in allowed),
        reverse=True,
    )
    return {"photos": photos}

# This helper is intended to be called by your existing Telegram bot handler.
# It stores only the photo bytes; connect it after reviewing your bot's code.
def save_photo_bytes(filename: str, content: bytes) -> str:
    safe_name = Path(filename).name
    suffix = Path(safe_name).suffix.lower()
    if suffix not in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        raise ValueError("Unsupported image type")
    if not content:
        raise ValueError("Empty image")
    target = UPLOAD_DIR / safe_name
    target.write_bytes(content)
    return f"/media/{safe_name}"

@app.get("/health")
async def health():
    return {"status": "ok"}
