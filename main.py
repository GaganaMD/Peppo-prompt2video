from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from backend.app.api import router

app = FastAPI()

# Add the CORS middleware
# This allows your frontend (e.g., hosted on Vercel) to make requests to this backend.
# For production, it's recommended to replace "*" with your specific frontend domain,
# e.g., ["https://your-frontend.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://peppo-prompt2video.vercel.app"], 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


# include API router
app.include_router(router)
