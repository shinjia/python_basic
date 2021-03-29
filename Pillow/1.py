from PIL import Image

im = Image.open('test.jpg')

print(im.format, im.size, im.mode)

im.show()
