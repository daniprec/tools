import os
import sys

from PIL import Image


def convert_png_to_pdf(folder_path, output_path):
    ls_files = sorted(os.listdir(folder_path))
    images = []
    for filename in ls_files:
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            images.append(image.convert("RGB"))

    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:])
        print("PDF file created successfully!")
    else:
        print("No PNG images found in the folder.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python png_to_pdf.py <folder_path> <output_path>")
        return

    folder_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_png_to_pdf(folder_path, output_path)


if __name__ == "__main__":
    main()
