# Peppo-prompt2video

# AI Video Generation App (Production Grade: FastAPI, React, Docker)

## Features
- Modular FastAPI backend (api, rag, cache, model)
- React frontend with live video streaming, regenerate, error fallback
- Wikipedia-powered RAG enrichment for prompts
- Local output caching (no duplicate API spend)
- Docker & Compose for easy deployment

## Getting Started

### 1. Backend
- `cd backend`
- Copy `.env.example` to `.env` and put your Replicate API token
- `docker build . -t ai-backend`
- `docker run --env-file .env -p 8000:8000 ai-backend`

### 2. Frontend
- `cd frontend`
- Copy `.env.example` to `.env` and set `REACT_APP_BACKEND_URL` for production
- `docker build . -t ai-frontend`
- `docker run -p 3000:80 ai-frontend`

### 3. Compose Everything
- From root: `docker-compose up --build`

## Deployment
- Backend: Render/Railway (Docker-native)
- Frontend: Vercel/Netlify or Docker host

## Security
- API keys in `.env`. Never commit `.env`.
- `.gitignore` covers secrets.

## Screenshots
- _(Add screenshots after deployment!)_

## Live Demo
- _(Provide public links after deployment)_

## License
CC
---

