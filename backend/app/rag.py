import requests

def enrich_prompt(prompt: str) -> str:
    """Basic RAG - add context from Wikipedia to your prompt, robust error handling."""
    entity = prompt.split()
    try:
        wiki = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{entity}")
        if wiki.ok and wiki.json().get("extract"):
            extract = wiki.json().get("extract", "")
            return f"{prompt}\nContext: {extract[:180]}"
        else:
            print(f"Wikipedia enrich failed for entity: {entity}, response: {wiki.text}")
    except Exception as e:
        print(f"Wikipedia API error: {str(e)}")
    return prompt
