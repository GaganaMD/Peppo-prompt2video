# app/cache.py
CACHE = {}

def get_from_cache(key):
    return CACHE.get(key)

def save_in_cache(key, value):
    CACHE[key] = value
