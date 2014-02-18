from PIL import Image

__author__ = 'Asus'
image_file = 'me.jpg'
img = Image.open(image_file)
# get the image's width and height in pixels
width, height = img.size
print(width, height)