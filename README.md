# Rafa Amin Gallery — starter project

This starter serves the separate `index.html` gallery and exposes `/api/photos`.

## Files
- `app.py` — FastAPI web backend and photo-list API
- `index.html` — editable gallery frontend
- `uploads/` — temporary image storage
- `requirements.txt`, `Procfile`, `railway.json` — Railway deployment setup
- `.env.example` — placeholder environment-variable names

## Local run

```bash
python -m pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`.

## Connect your existing Telegram bot

The Telegram bot code has not been included or modified because its source has not yet been supplied. After reviewing that code, call `save_photo_bytes(filename, content)` from the bot's photo handler to save a received image into `uploads/`. The gallery will then list it automatically.

Do not put bot tokens or API secrets in `index.html` or commit them to GitHub. Add them as Railway Variables. Railway's local filesystem is temporary; uploaded photos can disappear after restarts or redeployments.
