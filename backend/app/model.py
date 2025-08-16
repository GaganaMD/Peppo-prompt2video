import os
import requests
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# TEST MODE - set TEST_MODE = True for demo with a fixed video, False for actual generation
TEST_MODE = True  # Change to False for live model calls

def generate_video(enriched_prompt, duration=5):
    if TEST_MODE:
        # Use a free, always-available sample video for demo
        return "https://www.w3schools.com/html/mov_bbb.mp4", "Demo video."

    inference_url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "version": "60fdc6:be3dbbd728fb525f062b9b03fbe7d0046ec3e927d9f8ff6c96598251f54fa7e5",
        "input": {
            "prompt": enriched_prompt,
            "duration": duration,
            "fps": 24,
            "resolution": "720p",
            "aspect_ratio": "16:9",
            "camera_fixed": False
        }
    }
    try:
        resp = requests.post(inference_url, headers=headers, json=payload)
        print("Replicate response POST:", resp.text)
        if not resp.ok or "id" not in resp.json():
            return None, "Failed to start video generation."

        prediction_id = resp.json()["id"]
        import time
        for _ in range(60):
            poll = requests.get(f"{inference_url}/{prediction_id}", headers=headers)
            print("Replicate response POLL:", poll.text)
            res_json = poll.json()
            status_ = res_json.get("status")
            if status_ == "succeeded":
                video_url = res_json.get("output", [""])[0]
                return video_url, "Video generated."
            elif status_ == "failed":
                return None, "Video generation failed."
            time.sleep(2)
        return None, "Video generation timed out."
    except Exception as e:
        print("Replicate call failed:", str(e))
        return None, f"Error: {str(e)}"
