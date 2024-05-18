import cv2
import numpy as np
from PIL import Image
import pytesseract as pts
from pathlib import Path
import re
import os

ROOT_DIR = Path(__file__).parent
IMAGES_DIR = ROOT_DIR / 'images'
PROC_DIR = ROOT_DIR / 'processed_images'


def process_images():
    for image in IMAGES_DIR.iterdir():
        if image.suffix == '.jpg':
            no_extension_image = image.stem
            image_read = cv2.imread(str(image), 0)
            if image_read is None:
                print(f"Erro ao ler a imagem: {image}")
                continue
            _, processed_image = cv2.threshold(image_read, 128, 255, cv2.THRESH_BINARY)
            processed_image_path = PROC_DIR / f'{no_extension_image}_processed.jpg'
            cv2.imwrite(str(processed_image_path), processed_image)

def extract_number(numbers):
    for image in PROC_DIR.iterdir():
        if image.suffix == '.jpg':
            image_read = Image.open(image)
            text = pts.image_to_string(image_read)
            numbers.extend(re.findall(r'\d+', text))

numbers_list = []

process_images()
extract_number(numbers_list)
print(numbers_list)
