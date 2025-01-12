import inspect

from PIL import Image, ImageDraw, ImageFont
from numpy.random import dirichlet

logo = Image.open('logo.png')
print(logo.size)

# with Image.open(logo) as img_logo:
#     img_logo.load()

def resize_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//3, h//3))

img = Image.open('cat.jpg')
w, h = img.size
print(w,h)
signature = resize_photo('signature.png')
out = img
out.paste(signature, (0, 683))
out.save('out.jpg')

draw = ImageDraw.Draw(out)
font =ImageFont.truetype('Roboto_Condensed-Regular.ttf', 88)
draw.text((0,0), 'Hello World', font=font, fill='#DDF2EE')
# out.show()

