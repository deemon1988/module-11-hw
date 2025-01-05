import numpy as np
from PIL import Image

square1 = np.zeros((600, 600))
square1[150:350, 150:350] = 255
square2 = np.zeros((600, 600))
square2[200:400, 200:400] = 255

square1_array = np.asarray(square1)
square2_array = np.asarray(square2)

diff_array = square1_array - square2_array
diff_img = Image.fromarray(diff_array)
diff_img.show()

red = np.zeros((600, 600))
red[150:350, 150:350] = 255

green = np.zeros((600, 600))
green[200:400, 200:400] = 255

blue = np.zeros((600, 600))
blue[250:450, 250:450] = 255

red_img = Image.fromarray(red).convert("L")
green_img = Image.fromarray(green).convert("L")
blue_img = Image.fromarray(blue).convert("L")

square_img = Image.merge("RGB", (red_img, green_img, blue_img))
square_img.show()
