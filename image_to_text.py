import pytesseract
import os


def images_to_text(images_folder="page_jpegs"):
    # Get all preprocessed images
    images = [f for f in os.listdir(images_folder) if f.endswith("_preprocessed.jpeg")]
    
    # Ensure the directory exists
    os.makedirs('page_text', exist_ok=True)
    
    for image_name in images:
        image_path = os.path.join(images_folder, image_name)
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image_path)
        
        # Save the converted text to the page_text directory
        output_filename = image_name.replace("_preprocessed.jpeg", ".txt")
        with open(os.path.join('page_text', output_filename), 'w') as file:
            file.write(text)


if __name__ == "__main__":
    images_to_text()
