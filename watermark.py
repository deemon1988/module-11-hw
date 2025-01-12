import inspect
import os.path
from os import listdir
from os.path import exists

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def image_parameters(name):
    img = Image.open(name)
    print(img.format)
    print(img.mode)
    print(img.size)

def size_img(name):
    img = Image.open(name)
    w,h = img.size
    return w, h

def paste_text(images_path, font_name, output_path):
    font = ImageFont.truetype(font_name, 28)
    if not exists(output_path):
        os.mkdir(output_path)
    for img in listdir(images_path):
        image = os.path.join(images_path, img)
        with Image.open(image) as image_path:
            draw = ImageDraw.Draw(image_path)
            w, h = size_img(image)

            draw.text((0, (h-(font.size*2))), 'World of Magic', font=font, fill='#DDF2EE')
            #image_path.show()
            image_path.save(f'{output_path}/{img}')

def paste_logo(images_path, logo, output_path):
    if not exists(output_path):
        os.mkdir(output_path)
    for img in listdir(images_path):
        image = os.path.join(images_path, img)
        with Image.open(image) as image_path:
            if image_path.mode != 'RGBA':
                convert_image = image_path.convert('RGBA')
                img_logo = Image.open(logo)
                img_logo.resize((300, 300))
                image_size = size_img(image)
                logo_size = size_img(logo)
                paste_coord = tuple[int,int](x - y for x, y in zip(image_size, logo_size))
                convert_image.paste(img_logo, paste_coord, img_logo)
                convert_image = convert_image.convert('RGB')
                convert_image.save(f'{output_path}/{img}')

path_imgs = 'Elfs'
out_path_imgs = 'Elfs_logo'


#paste_logo(path_imgs, 'logo.png', out_path_imgs)
paste_text(path_imgs, 'PlaywriteAUSA-VariableFont_wght.ttf', out_path_imgs)
