from PIL import Image

im = Image.open('test.jpg')

box = (100, 150, 400, 300)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)

im.paste(region, box)

im.show()
