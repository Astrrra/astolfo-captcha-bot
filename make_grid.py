import random
import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
from config import rows, cols, output_width, output_height, lain_source, laint_source


def make_grid():
    output_image = Image.new("RGB", (output_width,output_height))

    lain_paths = []
    laint_paths = []
    for file in os.listdir(lain_source):
        lain_paths.append(os.path.join(lain_source, file))

    for file in os.listdir(laint_source):
        laint_paths.append(os.path.join(laint_source, file))

    lain = random.choice(lain_paths)
    laints = random.sample(laint_paths, k=3)

    tiles = laints.copy()
    tiles.append(lain)
    random.shuffle(tiles)
    tempTiles = tiles.copy()
    x_offset_step = int(output_width / cols)
    y_offset_step = int(output_height / rows)
    font = ImageFont.truetype("OpenSans-Bold.ttf", int(x_offset_step * 0.1))
    for row in range(rows):
        for col in range(cols):
            img = ImageOps.pad(ImageOps.contain(Image.open(tempTiles.pop(0)), (x_offset_step, y_offset_step)), (x_offset_step, y_offset_step), color="white")
            draw = ImageDraw.Draw(img)

            draw.ellipse((x_offset_step * 0.05, y_offset_step * 0.05, x_offset_step * 0.2, y_offset_step * 0.2), fill=(255,255,255), outline=(0,0,0), width=10)
            draw.text((x_offset_step * 0.1,y_offset_step * 0.05), str(rows+cols-len(tempTiles)), fill=(0,0,0), font=font)

            paste_box = (
                x_offset_step * col,
                y_offset_step * row,
                x_offset_step * (col + 1),
                y_offset_step * (row + 1)
            )
            output_image.paste(img, paste_box)
    return output_image, tiles
if __name__ == "__main__":
    make_grid()