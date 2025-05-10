import sys
import os
from pdf2image import convert_from_path

def pdf_to_jpg(pdf_path, output_dir):
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Convert PDF to a list of images
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            output_file = os.path.join(output_dir, f"page_{i + 1}.jpg")
            image.save(output_file, "JPEG")
            print(f"Saved: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python PDFtoJPG.py <PDF_PATH> [OUTPUT_DIR]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output_images"

    pdf_to_jpg(pdf_path, output_dir)