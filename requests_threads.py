import json
import os
import threading

import requests

GENIUS_API_URL = 'https://api.genius.com/search'
ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
imgs_links = []

response = requests.get(GENIUS_API_URL, params={
    'access_token': ACCESS_TOKEN, 'q': 'Kendrick Lamar'})
json_data = response.json()
print(json.dumps(json_data, indent=4, ensure_ascii=False))
for hit in json_data['response']['hits']:
    imgs_links.append(hit['result']['header_image_url'])


class ImageWriter(threading.Thread):
    def __init__(self, img_link):
        super().__init__()
        self.img_link = img_link

    def run(self):
        print(self.img_link)
        get_img = requests.get(self.img_link)
        img_name = os.path.basename(self.img_link)

        if not os.path.exists(f'album_images/{img_name}'):
            with open(f'album_images/{img_name}', 'wb') as img_file:
                img_file.write(get_img.content)
                print('Writed')
        else:
            print('Exists')


if not os.path.isdir('album_images'):
    os.mkdir('album_images')

writers = [ImageWriter(img_link=link) for link in imgs_links]
for writer in writers:
    writer.start()

for writer in writers:
    writer.join()

print("done")
