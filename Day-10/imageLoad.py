from diffusers import StableDiffusionPipeline
pipe=StableDiffusionPipeline.from_pretrained(
    "runwaymal/stable-diffusion-v1-5").to("cpu")
print("Success")