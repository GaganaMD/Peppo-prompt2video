import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Change to False to enable real video generation
TEST_MODE = False  

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
        # Replace with the actual version ID of your chosen model from Replicate
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
        # Start prediction
        resp = requests.post(inference_url, headers=headers, json=payload)
        print("Replicate response POST:", resp.text)
        if not resp.ok:
            return None, f"Failed to start generation: {resp.text}"

        data = resp.json()
        prediction_id = data.get("id")
        if not prediction_id:
            return None, "No prediction ID returned."

        # Poll until completion
        for _ in range(60):  # ~2 minutes max
            poll = requests.get(f"{inference_url}/{prediction_id}", headers=headers)
            res_json = poll.json()
            print("Replicate response POLL:", res_json)

            status_ = res_json.get("status")
            if status_ == "succeeded":
                output = res_json.get("output")
                if isinstance(output, list) and output:
                    return output[0], "Video generated."
                elif isinstance(output, str):
                    return output, "Video generated."
                else:
                    return None, "No video URL in output."
            elif status_ == "failed":
                return None, "Video generation failed."

            time.sleep(2)

        return None, "Video generation timed out."

    except Exception as e:
        print("Replicate call failed:", str(e))
        return None, f"Error: {str(e)}"
