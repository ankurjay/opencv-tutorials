import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# ------ IMAGE BLENDING ------

# Image blending is a type of Image aDdition, but different weights
# are given to the images in order to give a feeling of blending or
# transparency. 
# Images are added as per the equation:

# g(x) = (1 - beta) * img_1(x) + (beta) * img_2(x)

# Typically (1 - beta) is called 'alpha'.
# A third, scalar value called 'gamma' is also added to 
# each pixel's value after the blending is done


img1 = cv.imread('../data/ml.png')
img2 = cv.imread('../data/opencv-logo.png')

# Ensure images could be read
assert img1 is not None
assert img2 is not None 

# Resize the images so that their dimensions are same
width = img1.shape[1]
height = img1.shape[0]
img2 = cv.resize(img2, (width, height))

# Dimensions should be same
print(img1.shape, img2.shape)
assert(img1.shape == img2.shape)
assert(img1.dtype == img2.dtype)

ALPHA = 0.7
BETA = 1 - ALPHA
GAMMA = 40
blend = cv.addWeighted(img1, ALPHA, img2, BETA, GAMMA)

cv.imshow("Image 1", img1)
cv.imshow("Image 2", img2)
cv.imshow("Blended", blend)
cv.waitKey(0)
cv.destroyAllWindows()

