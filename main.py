# Takes everything from ./pics and turns them into ascii images

from PIL import Image
import os
import math
import codecs
import typing

# Returns the length of the pixel (3d vector - [r,g,b]) in colorspace
def getPixelIntensity(pixel: tuple):
    return math.sqrt(pixel[0]**2 + pixel[1]**2 + pixel[2]**2)

# rgb[0,0,0] is black (for reference)
# make sure to include the extension in the *input_name*
def pixel_wise_convert(characters: typing.List, input_name, output_name, thresholds=None):
    if thresholds == None: thresholds = [i/(len(characters))*441 for i in range(1, len(characters))] + [442]
    with codecs.open(os.path.join(os.path.curdir, f"text_pics/{output_name}.txt"), "w+", "utf-8") as f:
        img = Image.open(os.path.join(".", f"pics/{input_name}"))
        cursor = 0
        img_width = img.size[0]
        for pixel in list(img.getdata()):
            if cursor == img_width:
                f.write("\n")
                cursor = 0
            f.write(characters[[idx for idx, element in enumerate(thresholds) if (element > getPixelIntensity(pixel))][0]])
            cursor += 1

image_names = os.listdir("./pics")

# Darkest to the left, lightest to the right because the font is white
characters = ["∑", "∤", "∏", "∵"]

for image_name in image_names:
    pixel_wise_convert(characters, image_name, image_name[0:image_name.rfind(".")])
