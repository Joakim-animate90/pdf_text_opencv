# PDF Text Extraction with OpenCV

## Project Overview
This project is designed to extract text from images within PDF files using Python and OpenCV. The primary goal is to convert images to text, allowing for easy data extraction and analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd pdf_text_opencv
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Run the main script to process images and extract text:
  ```bash
  python main.py
  ```
- The script will process images and output the extracted text.

## OpenCV's Role
OpenCV is utilized in this project for preprocessing images extracted from PDFs. It enhances image quality to improve text extraction accuracy. The preprocessing includes converting images to grayscale, applying histogram equalization, blurring, and adaptive thresholding.

## Function Descriptions

1. **`convert_pdf_to_text(pdf_path)` in `main.py`**:
   - Converts a PDF file into images using `pdf_to_images`.
   - Extracts text from these images using `images_to_text`.
   - Returns the extracted text.

2. **`pdf_to_images(pdf_path, dpi=300, output_folder="page_jpegs")` in `image_splitter.py`**:
   - Converts each page of a PDF into a JPEG image.
   - Saves images in the specified output folder.
   - Calls `preprocess_image` to enhance each image for better text extraction.

3. **`preprocess_image(image_path)` in `image_splitter.py`**:
   - Reads an image and converts it to grayscale.
   - Enhances contrast using CLAHE.
   - Applies Gaussian blur to reduce noise.
   - Uses adaptive thresholding to create a binary image.
   - Saves the preprocessed image for OCR.

4. **`images_to_text(images_folder="page_jpegs")` in `image_to_text.py`**:
   - Reads preprocessed images from a folder.
   - Uses Tesseract OCR to extract text from each image.
   - Saves the extracted text to a file.

## File Descriptions
- `main.py`: The main script to run the text extraction process.
- `image_to_text.py`: Contains functions to convert images to text using OCR.
- `image_splitter.py`: Handles splitting images if necessary for processing.
- `requirements.txt`: Lists all Python dependencies required for the project.

## Dependencies
- Python 3.x
- OpenCV
- Tesseract OCR (ensure it's installed and configured on your system)

## Notes
- Ensure that Tesseract OCR is correctly installed on your system for the text extraction to work.
- Adjust the scripts as necessary to fit your specific PDF and image processing needs.
