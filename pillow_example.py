import os.path
import random
from os import mkdir

import requests
from PIL import Image, ImageFilter

size = 'width=1920&height=1080'
category = 'nature'
API_URL = f'https://api.api-ninjas.com/v1/randomimage?category={category}&{size}'
API_KEY = '2Xqk5vZALiwq7gtzVujwKg==GWkQ7byqKApF973g'

counter = 0
extension = 'jpg'

response = requests.get(API_URL, headers={'X-Api-Key': API_KEY, 'Accept': f'image/{extension}'})

if response.status_code == requests.codes.ok:
    if not os.path.isdir('random_images'):
        mkdir('random_images')
    counter += 1
    with open(f'random_images/img_{category}_{counter}.{extension}', 'wb') as img:
        img.write(response.content)
else:
    print(response.status_code)
path = 'random_images'
rand_img = random.choice([f'{path}/{img}' for img in os.listdir(path)])
print(rand_img)

with Image.open(rand_img) as image:
    image.load()

# image.show()
print(image.size)
print(image.format)
print(image.mode)

cropped_img = image.crop((100, 300, 800, 1000))
print(cropped_img.size)
# cropped_img.show()

# low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
# low_res_img.show()

low_res_img = cropped_img.reduce(2)
low_res_img.show()

# cropped_img.thumbnail((640, 480))
# cropped_img.show()

cropped_img.save('random_images/cropped_img.jpg')

converted_img = image.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.show()

rotated_img = image.rotate(45)
rotated_img.show()

blur_img = image.filter(ImageFilter.GaussianBlur(20)).show()
img_gray = image.convert('L')
edges = img_gray.filter(ImageFilter.FIND_EDGES).show()
