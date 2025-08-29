
# BFHL API (FastAPI)

A minimal FastAPI app implementing the **/bfhl** POST endpoint per the VIT Full Stack question paper.

## 1) Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

# Optionally set your details (recommended):
# PowerShell (Windows):
$env:FULL_NAME_LOWER="rishita_nigam"
$env:DOB_DDMMYYYY="14062003"
$env:EMAIL="your_email@vit.ac.in"
$env:ROLL_NUMBER="YOUR_ROLL"

# Bash (macOS/Linux):
# export FULL_NAME_LOWER="rishita_nigam"
# export DOB_DDMMYYYY="14062003"
# export EMAIL="your_email@vit.ac.in"
# export ROLL_NUMBER="YOUR_ROLL"

uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Test with `curl`:

```bash
curl -X POST http://localhost:8000/bfhl ^
  -H "Content-Type: application/json" ^
  -d "{\"data\":[\"a\",\"1\",\"334\",\"4\",\"R\",\"$\"]}"
```

## 2) Run tests (local checks)

```bash
pytest -q
```

## 3) Deploy to Render (easy)

1. Push this folder to a **public GitHub repo**.
2. On [Render](https://render.com), **New +** → **Web Service** → connect your repo.
3. Pick environment **Python**.
4. **Start command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add **Environment Variables**: `FULL_NAME_LOWER`, `DOB_DDMMYYYY`, `EMAIL`, `ROLL_NUMBER`.
6. Deploy. Note the public URL, e.g. `https://your-service.onrender.com`.

Your final endpoint to submit must be: `https://your-service.onrender.com/bfhl`

## 4) Deploy to Railway (alternative)

1. Push to GitHub, then on [Railway](https://railway.app) → **New Project** → **Deploy from GitHub**.
2. Add the same environment variables as above.
3. Set **Start Command** to `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
4. Deploy and use `https://your-app.up.railway.app/bfhl`

## 5) Notes

- Numbers are returned as **strings** in all arrays and `sum`.
- Alphabetic tokens are uppercased in `alphabets`.
- `concat_string` is built from **all alphabetic characters** present in the input (including inside mixed tokens), reversed, with **alternating caps** (Upper, lower, Upper, ...).
- Always returns HTTP 200 with `is_success: true/false` in the JSON body.
