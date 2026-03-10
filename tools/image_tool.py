from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0"
)

pipe.to("cpu")

async def run(prompt):

    image = pipe(prompt).images[0]

    path = f"generated/{prompt[:10]}.png"
    image.save(path)

    return path