import inspect
import os
from pprint import pprint

import requests
from PIL import Image

simple_str = 'Hello World'
simpe_number = 12


class Picture:
    def __init__(self, url, path):
        self.url = url
        self.name = 'img_1.jpg'
        self.path = path

    def get_picture(self):
        response = requests.get(self.url)
        if not os.listdir(self.path):
            os.mkdir(self.path)
        content = response.content
        with open(f'{self.path}/{self.name}', 'wb') as img:
            img.write(content)

    def show_picture(self):
        os.chdir(self.path)
        image = Image.open(self.name)
        image.show()


RANDOM_IMAGE_URL = 'https://random-image-pepebigotes.vercel.app/api/random-image'
simple_picture = Picture(url=RANDOM_IMAGE_URL, path='random_images')
simple_picture.get_picture()


# simple_picture.show_picture()

def inspect_attr(object, cls, attr):
    data = {}
    if isinstance(object, cls):
        data[attr] = hasattr(object, attr)
        data['value'] = getattr(object, attr)
        print('\n')
        pprint(data)


def introspekcia(object):
    data = {}
    data['Тип объекта'] = type(object)
    try:
        data['Имя'] = object.__name__
    except AttributeError as ex:
        print(ex)
    data['Атрибуты объекта'] = dir(object)
    data['Модуль'] = inspect.getmodule(object)
    data['Методы'] = inspect.getmembers(object, predicate=inspect.ismethod)
    data['Функции'] = inspect.getmembers(object, predicate=inspect.isfunction)
    print('\n')
    pprint(data)


introspekcia(simple_str)
introspekcia(simple_picture)
introspekcia(requests)
inspect_attr(simple_picture, Picture, 'url')
