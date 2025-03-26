import os
import cv2
from pdf2image import convert_from_path


def pdf_to_images(pdf_path, dpi=300, output_folder="page_jpegs"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(f"Converting PDF to images with DPI={dpi}...")
    images = convert_from_path(pdf_path, dpi=dpi, fmt="jpeg")
    total_pages = len(images)
    digits = len(str(total_pages))

    for i, image in enumerate(images):
        image_path = os.path.join(
            output_folder, f"Page_{str(i + 1).zfill(digits)}.jpeg"
        )
        image.save(image_path, "JPEG")
        print(f"Page {i + 1} saved as image: {image_path}")

        # Preprocess the image
        preprocess_image(image_path)




def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Contrast Limited Adaptive Histogram Equalization (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)

    # Use adaptive thresholding instead of Otsu
    binary = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )

    # Save the preprocessed image
    preprocessed_path = image_path.replace(".jpeg", "_preprocessed.jpeg")
    cv2.imwrite(preprocessed_path, binary)
    print(f"Preprocessed image saved: {preprocessed_path}")

    return preprocessed_path



if __name__ == "__main__":
    pdf_path = "convert-to-markdown.pdf"
    pdf_to_images(pdf_path)
    print("PDF conversion to JPEG images complete.")