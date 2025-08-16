import requests

def enrich_prompt(prompt: str) -> str:
    """RAG-style prompt enrichment from Wikipedia."""
    entity = prompt.split()[0]
    try:
        wiki = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{entity}")
        if wiki.ok:
            extract = wiki.json().get("extract", "")
            if extract:
                return f"{prompt}\nContext: {extract[:180]}"
    except Exception:
        pass
    return prompt
