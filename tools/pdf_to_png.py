import sys

import PyPDF2
from pdf2image import convert_from_path


def convert_pdf_to_png(pdf_path, output_folder):
    try:
        # Extract images from PDF
        images = convert_from_path(pdf_path)

        # Save each image as a PNG
        for i, image in enumerate(images):
            image.save(f"{output_folder}/page_{i + 1:03}.png", "PNG")

        print(f"Successfully converted {len(images)} pages to PNG.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <pdf_path> <output_folder>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_folder = sys.argv[2]

    convert_pdf_to_png(pdf_path, output_folder)
