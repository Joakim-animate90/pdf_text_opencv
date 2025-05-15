import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def setup_openai_client():
    """Initialize OpenAI client."""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY in .env file")
    
    return OpenAI(api_key=api_key)

def encode_image_to_base64(image_path):
    """Convert image to base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def extract_and_process_text(client, image_path):
    """Extract and process text from image using GPT-4 Vision."""
    base64_image = encode_image_to_base64(image_path)
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert at OCR and document formatting. Extract all text from the image, preserve the formatting, and fix any obvious OCR errors."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract all text from this image. Preserve paragraphs, lists, and table structures. Fix any obvious OCR errors."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=10000
    )
    
    return response.choices[0].message.content

def process_images(images_folder="page_jpegs", output_folder="page_text_ai"):
    """Process all preprocessed images using GPT-4 Vision."""
    # Setup OpenAI client
    client = setup_openai_client()
    
    # Create output directory
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each preprocessed image
    images = [f for f in os.listdir(images_folder) if f.endswith("_preprocessed.jpeg")]
    
    for image_name in images:
        image_path = os.path.join(images_folder, image_name)
        print(f"Processing {image_name}...")
        
        # Extract and process text using GPT-4 Vision
        processed_text = extract_and_process_text(client, image_path)
        
        # Save results
        output_filename = image_name.replace("_preprocessed.jpeg", "_ai.txt")
        with open(os.path.join(output_folder, output_filename), 'w') as file:
            file.write(processed_text)
        print(f"Saved processed text to {output_filename}")

if __name__ == "__main__":
    process_images()
