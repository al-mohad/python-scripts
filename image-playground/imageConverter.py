import sys
import os
from PIL import Image

# Grab args
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# Check if 'new' folder exist else create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print('Output folder is not found, but it has been created!')
# Loop through the selected folder of images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    # clean file name
    clean_name = os.path.splitext(filename)[0]
    # convert images to png
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print(f'{filename} converted to png!')
# save the converted images to 'new' folder
