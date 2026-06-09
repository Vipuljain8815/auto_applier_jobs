import requests
from io import BytesIO
from PIL import Image
import pytesseract
import re

def extract_text_from_image(image_url):
    """
    Downloads an image from a URL and extracts text using Tesseract OCR.
    """
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            # Optional: Image preprocessing for better OCR could be added here
            # e.g., converting to grayscale or thresholding
            text = pytesseract.image_to_string(image)
            return text
        else:
            return ""
    except Exception as e:
        print(f"Error fetching or processing image: {e}")
        return ""
