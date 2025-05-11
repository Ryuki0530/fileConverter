import sys
import os
from pdf2image import convert_from_path  # type: ignore

def convertPdfToJpg(pdf_path, start_page_num=None, end_page_num=None):
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return 1

    output_dir = os.getcwd()

    try:
        if start_page_num is not None and end_page_num is not None:
            images = convert_from_path(pdf_path, first_page=start_page_num, last_page=end_page_num)
            base_page_num = start_page_num
        elif start_page_num is not None:
            images = convert_from_path(pdf_path, first_page=start_page_num, last_page=start_page_num)
            base_page_num = start_page_num
        else:
            images = convert_from_path(pdf_path)
            base_page_num = 1

        for i, image in enumerate(images):
            output_file = os.path.join(output_dir, f"page_{base_page_num + i}.png")
            image.save(output_file, "PNG")
            print(f"Saved: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <PDF_PATH> [START_PAGE_NUM] [END_PAGE_NUM]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    start_page_num = int(sys.argv[2]) if len(sys.argv) > 2 else None
    end_page_num = int(sys.argv[3]) if len(sys.argv) > 3 else None

    result = convertPdfToJpg(pdf_path, start_page_num=start_page_num, end_page_num=end_page_num)
    sys.exit(result)
