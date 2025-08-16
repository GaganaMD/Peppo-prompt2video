# Peppo-prompt2video

## 📝 Project Overview

This is a minimal, scalable, and production-grade web application that generates **5–10 second AI videos** from user prompts. Built with a modern modular stack (**React, FastAPI, Docker**), it features prompt enrichment, caching, error handling, and a smooth streaming UI.

* **Frontend:** React (prompt entry, streaming video, error/loading handling, regenerate option, fallback demo video)
* **Backend:** FastAPI (modular, Replicate API integration, RAG-style enrichment with Wikipedia, caching, logging)
* **DevOps:** Docker & Docker Compose (for local and cloud deployment)
* **Model:** Replicate **SeedANCE-1-Lite**, with fallback demo video for testing

---

## 🖥️ Features

* ✅ Text prompt input (with length validation)
* ✅ **RAG prompt enrichment**: Wikipedia context injection
* ✅ **AI video generation** (5–10s via Replicate)
* ✅ Video preview & streaming (not just downloads)
* ✅ **Regenerate button** (retry same or new prompt seamlessly)
* ✅ Smart error handling & fallback demo video
* ✅ Caching to prevent duplicate model calls
* ✅ Modular FastAPI + React + Docker architecture
* ✅ Stateless backend, concurrent users supported
* ✅ Security-first: API keys stored only in `.env`

---

## 📈 Demo & Screenshots

| UI Example                          | Description               |
| ----------------------------------- | ------------------------- |
| ![Demo Screenshot](assets/demo1.gif) | Prompt-to-video in action |

Full-quality demo available here: [🎬 Demo Video](assets/Demo%20recordings.mp4)

---

## 🗂 Directory Structure

```
ai-video-app/
├── backend/
│   ├── app/        # api.py, rag.py, cache.py, model.py
│   ├── main.py
│   ├── requirements.txt, Dockerfile, .env
├── frontend/
│   ├── public/placeholder.mp4
│   ├── src/App.js, index.js
│   ├── package.json, Dockerfile, .env
├── docker-compose.yml
```

---

## 🛠️ Tech Stack

* **Frontend:** React, HTML5 Video, JavaScript, Docker
* **Backend:** Python, FastAPI (modular), Docker
* **AI Model:** SeedANCE-1-Lite via Replicate API
* **RAG:** Wikipedia summary API
* **DevOps:** Docker, Docker Compose

---

## ⚡ Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/GaganaMD/Peppo-prompt2video.git
cd Peppo-prompt2video
```

### 2. Backend Setup

Using Docker:

```bash
cd backend
cp .env.example .env   # Add your Replicate API key
docker build -t ai-backend .
docker run --env-file .env -p 8000:8000 ai-backend
```

Or with Python:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Frontend Setup

Using Docker:

```bash
cd ../frontend
cp .env.example .env
npm install
docker build -t ai-frontend .
docker run -p 3000:80 ai-frontend
```

Or with Node:

```bash
npm start
```

### 4. (Optional) Run Both with Compose

```bash
docker-compose up --build
```

---

## 🌐 Deployment

Recommended:

* **Backend:** Render or Railway with Dockerfile
* **Frontend:** Vercel, Netlify, or Docker host

Configuration:

* Set your Replicate API key in backend cloud dashboard (`.env`).
* Update frontend `.env`: `REACT_APP_BACKEND_URL` → your backend public URL.

---

## 🔑 API Key Security

* Your **Replicate API key** lives in `backend/.env` (never in code).
* `.gitignore` ensures secrets are safe.

---

## ✅ Rubric Coverage

* **Functionality:** Prompt → Model/API → Video preview (fallback included)
* **Deployment:** Docker-ready, cloud deployable
* **Code Quality:** Modular, documented, `.env` for secrets
* **Docs:** Comprehensive README (this file ✨)
* **Innovation:** RAG enrichment, caching, regenerate, streaming UI, extensibility

---

## 🚀 Future Developments

Planned or potential upgrades:

* Advanced streaming (chunked/adaptive for large videos)
* Authentication & video history
* Batch/queued generation
* Multi-model support (Stable Video Diffusion, Runway, Pika, open-source)
* Browser-based video editing (trim, filters, overlays)
* Self-hosted AI models (no 3rd-party dependency)
* Tailwind UI polish, accessibility, mobile-first
* Enhanced RAG (better context extraction, multi-source)
* Persistent caching/DB for analytics
* Social sharing, longer duration videos

---

## 👩💻 License

This project is licensed under the **Creative Commons License (CC BY 4.0)**.
You are free to share and adapt the work, provided proper attribution is given.

---

## 📬 Contact

* **Issues/Contributions:** GitHub Issues
* **Feedback/Questions:** gagana.md.work@gmail.com

---

✨ Enjoy turning prompts into videos with AI magic! If you build upon this project, please link back or contribute. 🚀
