import cv2
from PIL import Image
import pytesseract as pts
from pathlib import Path
import re


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


def extract_number(numbers, numbers_list_converted, excluded_numbers): 
    process_images()

    with open("exclude.txt", "r") as file:
        excluded_numbers = file.read().splitlines()
    excluded_numbers = [number.replace(" ", "").replace("-", "") for number in excluded_numbers]

    phone_pattern = re.compile(r'\b\d{2}\s\d{2}\s\d{4,5}-\d{4}\b')
    for image in PROC_DIR.iterdir():
        if image.suffix == '.jpg':
            image_read = Image.open(image)
            text = pts.image_to_string(image_read)
            numbers.extend(phone_pattern.findall(text))

    numbers_list_converted = [number.replace(" ", "").replace("-", "") for number in numbers]
    for number in excluded_numbers:
        if number in numbers_list_converted:
            numbers_list_converted.remove(number)
