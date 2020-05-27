# Install Pillow Library
from PIL import Image, ImageFilter
# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('./filtered_images/pikachu_cropped.png', 'png')
# filtered_img.save('./filtered_images/pikachu_cropped.png', 'png')
# filtered_img.show()


img = Image.open('./images/astro.jpg')
# new_img = img.resize((400, 400))
# new_img.save('./filtered_images/thumbnail.jpg')
img.thumbnail((400, 400))
img.save('./filtered_images/thumbnail2.jpg')
