import os

import typer
from PIL import Image


def upscale_image(file_path: str, scale_factor: int = 4):
    # Load the image
    image = Image.open(file_path)

    # Calculate the new dimensions
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    new_width = int(original_width * scale_factor)
    new_height = int(new_width / aspect_ratio)

    # Upscale the image
    upscaled_image = image.resize((new_width, new_height))

    # Save the upscaled image
    # Get the file path and name
    file_name, file_ext = os.path.splitext(file_path)
    # Construct the new file path
    upscaled_file_path = file_name + "-upscaled" + file_ext

    # Save the upscaled image
    upscaled_image.save(upscaled_file_path)


def main(file_path: str, scale_factor: int = 4):
    upscale_image(file_path=file_path, scale_factor=scale_factor)


if __name__ == "__main__":
    typer.run(main)
