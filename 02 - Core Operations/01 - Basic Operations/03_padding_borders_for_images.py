import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys

BLUE = [255, 0, 0]
BORDER_WIDTH = 20

# Read the Image
img = cv.imread('../data/opencv-logo.png')

# Check if the image was loaded correctly
if img is None:
    sys.exit("Could not read the image!")

# We use cv.copyMakeBorder() to make borders
# We specify top, bottom, left, right border width in pixels, as args
# We also specify a border type, and a color of border (if applicable)


# There are multiple types of borders that can be added.

# cv.BORDER_CONSTANT : a constant colored border
constant = cv.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv.BORDER_CONSTANT, value=BLUE)

# cv.BORDER_REFLECT : reflect the border elements e.g.  cba | abcdefghi | ihg
reflect = cv.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv.BORDER_REFLECT)

# cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT
# Same as BORDER_REFLECT but does not include the border element 
# e.g. cb | abcdefghi | hg
reflect101 = cv.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv.BORDER_REFLECT_101)

# cv.BORDER_REPLICATE : Zero-order hold on the border element
# i.e. the border element is replicated e.g. aaaa | abcdef | ffff
replicate = cv.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv.BORDER_REPLICATE)

# cv.BORDER_WRAP : Periodicity e.g. ghi | abcdefghi | abc
wrap = cv.copyMakeBorder(img, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, BORDER_WIDTH, cv.BORDER_WRAP)


# OpenCV operates on images in B,G,R format, however,
# Matplotlib expects R,G,B. So we need to convert the
# above images.
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
constant = cv.cvtColor(constant, cv.COLOR_BGR2RGB)
reflect = cv.cvtColor(reflect, cv.COLOR_BGR2RGB)
reflect101 = cv.cvtColor(reflect101, cv.COLOR_BGR2RGB)
replicate = cv.cvtColor(replicate, cv.COLOR_BGR2RGB)
wrap = cv.cvtColor(wrap, cv.COLOR_BGR2RGB)



# Display all these in subplots
plt.subplot(231)
plt.imshow(img,'gray')
plt.title('ORIGINAL')
plt.subplot(232)
plt.imshow(replicate,'gray')
plt.title('REPLICATE')
plt.subplot(233)
plt.imshow(reflect,'gray')
plt.title('REFLECT')
plt.subplot(234)
plt.imshow(reflect101,'gray')
plt.title('REFLECT_101')
plt.subplot(235)
plt.imshow(wrap,'gray')
plt.title('WRAP')
plt.subplot(236)
plt.imshow(constant,'gray')
plt.title('CONSTANT')
 
plt.show()