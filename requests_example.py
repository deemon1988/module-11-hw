import json
import os.path
from os import mkdir

import requests
from PIL import Image
from queue import Queue, Empty

GENIUS_URL = 'https://api.genius.com/'
GENIUS_API_URL = 'https://api.genius.com/search'
ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'


def simple_request(url):
    response = requests.get(GENIUS_URL)
    html_data = response.text
    print(html_data)
    print(response.encoding)
    print(response.headers.get('Content-Type'))


class SimpleParser():
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token
        self.images_url = []
        self.counter = 0

    def __access_request(self, api_url, access_token):
        response = requests.get(api_url, params={'access_token': access_token, 'q': 'Kendrick Lamar'})
        json_data = response.json()
        print(json.dumps(json_data, indent=4, ensure_ascii=False))
        if json_data:
            self.__process_json(json_data)

    def __process_json(self, json_data):
        while True:
            try:
                img_url = json_data['response']['hits'][self.counter]['result']['header_image_url']
                if not img_url in self.images_url:
                    self.images_url.append(img_url)
                self.counter += 1
            except IndexError:
                break
        print(self.images_url)

    def get_images(self):
        self.__access_request(self.base_url, self.access_token)

        if not os.path.isdir('images'):
            mkdir('images')

        for image_url in self.images_url:
            image_name = os.path.basename(image_url)

            if not os.path.exists(f'images/{image_name}'):
                get_image = requests.get(image_url)
                with open(f'images/{image_name}', 'wb') as f:
                    f.write(get_image.content)
            else:
                print(f'File {image_name} ready exists')


class ImageRedactor():
    def __init__(self, queue):
        self.queue = queue

    def change_color(self):
        counter = 0
        if not os.path.isdir('re_images'):
            mkdir('re_images')

        while True:
            try:
                counter += 1
                image_path, image = self.queue.get(timeout=1)
                extension = os.path.splitext(image)[1]
            except Empty:
                break
            image = Image.open(f'{image_path}/{image}')
            image_name = f'image_{counter}_{image.size}{extension}'
            image = image.convert('L')
            image.save(f're_images/image_{counter}_{image.size}{extension}')


if __name__ == '__main__':
    content = SimpleParser(GENIUS_API_URL, ACCESS_TOKEN)
    content.get_images()

    queue = Queue()
    images_path = 'images'
    for image in os.listdir(images_path):
        queue.put((images_path, image))

    re_image = ImageRedactor(queue)
    re_image.change_color()
