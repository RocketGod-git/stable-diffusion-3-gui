# __________                  __             __     ________             .___ 
# \______   \  ____    ____  |  | __  ____ _/  |_  /  _____/   ____    __| _/ 
#  |       _/ /  _ \ _/ ___\ |  |/ /_/ __ \\   __\/   \  ___  /  _ \  / __ |  
#  |    |   \(  <_> )\  \___ |    < \  ___/ |  |  \    \_\  \(  <_> )/ /_/ |  
#  |____|_  / \____/  \___  >|__|_ \ \___  >|__|   \______  / \____/ \____ |  
#         \/              \/      \/     \/               \/              \/  
#
# Stable Diffusion 3 GUI by RocketGod
#
# https://github.com/RocketGod-git/stable-diffusion-3-gui


import torch
from diffusers import StableDiffusion3Pipeline
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import ImageTk
import logging
from huggingface_hub import login

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Authenticate to Hugging Face ---> EDIT THIS TOKEN ONLY! <---
access_token = "YOUR-TOKEN-FROM-HUGGING-FACE-GOES-HERE"
login(access_token)


# Load the Stable Diffusion model
pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
pipe = pipe.to("cuda")


def generate_image():
    prompt = prompt_text.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Warning", "Please enter a prompt.")
        return

    try:
        result = pipe(
            prompt,
            negative_prompt="",
            num_inference_steps=28,
            guidance_scale=7.0
        )
        image = result.images[0]
        
        image_tk = ImageTk.PhotoImage(image)
        image_label.config(image=image_tk)
        image_label.image = image_tk  # keep a reference
        logging.info("Image generated and displayed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        logging.error(f"Error occurred: {str(e)}")

# GUI STUFF
window = tk.Tk()
window.title("Stable Diffusion Image Generator")
window.geometry("800x600")  # Set the window size

prompt_label = tk.Label(window, text="Enter a prompt:")
prompt_label.pack(pady=(10, 0))
prompt_text = scrolledtext.ScrolledText(window, width=70, height=4)
prompt_text.pack(pady=(0, 10))

generate_button = tk.Button(window, text="Generate Image", command=generate_image)
generate_button.pack(pady=(0, 10))

image_label = tk.Label(window)
image_label.pack(pady=(10, 0))


window.mainloop()