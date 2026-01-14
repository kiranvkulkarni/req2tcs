
import pytesseract
from PIL import Image
def extract_text(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return [t.strip() for t in text.splitlines() if t.strip()]
