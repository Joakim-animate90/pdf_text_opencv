import os
from image_splitter import pdf_to_images
from image_to_text import images_to_text


def convert_pdf_to_text(pdf_path):
    # Convert PDF to images and preprocess them
    pdf_to_images(pdf_path)
    print("PDF conversion and preprocessing completed.")

    # Convert preprocessed images to text
    text = images_to_text()
    print("Text extraction from images completed.")

    return text


def main():
    pdf_path = "joakim2.pdf"
    text = convert_pdf_to_text(pdf_path)
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    main()
