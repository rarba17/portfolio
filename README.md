# Portfolio (FastAPI + Vue 3 + Pinia)

Design-led personal portfolio with a custom frontend and a production-ready API backend.

## Stack

- Backend: FastAPI, REST endpoints, SMTP contact delivery, in-memory rate limiting, CORS
- Frontend: Vue 3 + Pinia + Tailwind (custom CSS-driven layout and motion)
- Production serving: FastAPI serves `frontend/dist` static output when built

## Project Structure

```
portfolio/
├── backend/
│   ├── .env.example
│   ├── app/
│   │   ├── api/router.py
│   │   ├── core/config.py
│   │   ├── data/content.py
│   │   ├── models/schemas.py
│   │   ├── services/contact.py
│   │   ├── services/rate_limit.py
│   │   └── main.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── .env.example
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── src/
│       ├── App.vue
│       ├── main.js
│       ├── style.css
│       ├── components/
│       │   ├── IntroTerminal.vue
│       │   └── ProjectRail.vue
│       └── stores/
│           └── portfolio.js
├── public/
│   └── resume.pdf
└── .gitignore
```

## API Endpoints

- `GET /api/health`
- `GET /api/projects`
- `GET /api/articles`
- `POST /api/contact` (expects `multipart/form-data`)
- `GET /api/resume` (downloads `public/resume.pdf`)

## Environment Setup

1. Backend env:
   - Copy `backend/.env.example` to `backend/.env`
   - Fill SMTP and contact email values

2. Frontend env:
   - Copy `frontend/.env.example` to `frontend/.env`
   - Set `VITE_API_BASE_URL`:
     - dev: `http://localhost:8000`
     - production same-origin: leave blank

## Run in Development

### 1) Start backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Start frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## Production Build (single app served by FastAPI)

```bash
cd frontend
npm install
npm run build
```

Then run API:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

When `frontend/dist` exists, FastAPI serves:
- `index.html` at `/`
- static assets at `/assets/*`
- SPA fallback for non-API routes

## Notes

- `public/resume.pdf` is a placeholder; replace with your real resume file.
- Contact rate limit is configurable via:
  - `CONTACT_RATE_LIMIT`
  - `CONTACT_RATE_WINDOW_SECONDS`
- SMTP settings are optional in local dev. If unset, contact requests still return success.
