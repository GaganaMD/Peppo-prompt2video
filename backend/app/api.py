from fastapi import APIRouter
from pydantic import BaseModel
from app.cache import get_from_cache, save_in_cache
from app.rag import enrich_prompt
from app.model import generate_video

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    duration: int = 5

@router.get("/")
def health_check():
    return {"message": "Video Generation API is running."}

@router.post("/generate")
def generate_endpoint(req: PromptRequest):
    prompt = req.prompt.strip()
    duration = min(max(req.duration, 5), 10)
    if len(prompt) < 3:
        return {"message": "Prompt must be at least 3 characters."}

    cache_key = prompt + str(duration)
    cached = get_from_cache(cache_key)
    if cached:
        return {"video_url": cached, "message": "Served from cache."}

    enriched = enrich_prompt(prompt)
    print(f"Calling model with enriched prompt: {enriched[:90]}...")

    video_url, msg = generate_video(enriched, duration)
    if video_url:
        save_in_cache(cache_key, video_url)
        return {"video_url": video_url, "message": msg}
    else:
        print(f"Video generation failed: {msg}")
        return {"message": msg}
