import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def detect_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = "text.jpg"

    print("Current Working Directory:", os.getcwd())
    print("Looking for image at:", os.path.abspath(image_path))
    print("File exists:", os.path.isfile(image_path))

    try:
        img = Image.open(image_path)
        img.show()  # This opens the image in Preview or default viewer on Mac

        detected_text = detect_text(image_path)
        print("Detected Text:")
        print(detected_text)
    except Exception as e:
        print(f"Error: {e}")
