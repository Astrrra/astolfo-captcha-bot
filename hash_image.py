from PIL import Image
from config import lain_source, laint_source
import os


filename_to_hash = {}
hash_is_lain = {}


def hash_image(img: Image)-> str:
    img = img.resize((10, 10), Image.ANTIALIAS)
    img = img.convert("L")
    pixel_data = list(img.getdata())
    avg_pixel = sum(pixel_data)/len(pixel_data)
    bits = "".join(['1' if (px>= avg_pixel) else '0' for px in pixel_data])
    hex_representation = str(hex(int(bits, 2)))[2:][::-1].upper()
    return hex_representation


for file in os.listdir(lain_source):
    filename = os.path.join(lain_source, file)
    hash = hash_image(Image.open(filename))
    filename_to_hash[filename] = hash
    hash_is_lain[hash] = True

for file in os.listdir(laint_source):
    filename = os.path.join(laint_source, file)
    hash = hash_image(Image.open(filename))
    filename_to_hash[filename] = hash
    hash_is_lain[hash] = False
