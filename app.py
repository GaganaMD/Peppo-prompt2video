import os
import torch
from PIL import Image
import streamlit as st
import tempfile
import imageio
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline

# Streamlit UI setup
st.set_page_config(page_title="Prompt to Video AI", layout="centered")
st.title("Prompt to Video AI Generator🎬")

prompt = st.text_input("Enter your prompt for video:", max_chars=120)
generate = st.button("Generate Video")

if "video_path" not in st.session_state:
    st.session_state["video_path"] = None

def generate_image(prompt_text):
    with st.spinner("Generating image..."):
        sd_pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1-base", torch_dtype=torch.float16
        ).to("cuda")
        image_out = sd_pipe(prompt_text).images[0]
        return image_out

def image_to_video(image_pil):
    with st.spinner("Animating image to video..."):
        svd_pipe = StableVideoDiffusionPipeline.from_pretrained(
            "stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16
        ).to("cuda")
        video_out = svd_pipe(image_pil)   # returns object with 'frames'
        frames = video_out.frames         # list of PIL Images
        return frames

def save_video(frames, fps=8):
    # Save frames to MP4 in a temp file
    temp_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
    imageio.mimsave(temp_file.name, [f.convert("RGB") for f in frames], fps=fps)
    return temp_file.name

# Main generation pipeline
if generate and prompt:
    try:
        image = generate_image(prompt)
        frames = image_to_video(image)
        video_path = save_video(frames, fps=8)
        st.session_state["video_path"] = video_path
        st.success("Video generated!")
    except Exception as e:
        st.error(f"Error: {e}")

# Display video result
if st.session_state["video_path"]:
    st.video(st.session_state["video_path"], format="video/mp4")

st.caption("Built with Stable Diffusion + Stable Video Diffusion | GPU required")
