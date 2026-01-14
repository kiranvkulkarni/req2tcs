"""
OCR abstraction using Tesseract.
"""

from PIL import Image
import pytesseract
from typing import List


def extract_text(image_path: str) -> List[str]:
    image = Image.open(image_path)
    raw_text = pytesseract.image_to_string(image)

    return [
        line.strip()
        for line in raw_text.splitlines()
        if line.strip()
    ]
