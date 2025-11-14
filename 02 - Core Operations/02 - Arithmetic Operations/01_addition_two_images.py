import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# ------ IMAGE ADDITION ------

# Image addition can be done using cv.add() or numpy addition
# cv.add() is a saturated operation
# numpy addition is a modulo operation
# The dtype and dimensions of both images should be the same.
# Or, the second image can simply be a scalar value.

# Here is the difference between cv.add() and numpy
# addition, performed on a scalar valued array.

x = np.uint8([250])
y = np.uint8([10])

print("CV Addition of 250 and 10 gives : ", cv.add(x,y))
print("Numpy addition of 250 and 10 gives : ", x + y)

# Prefer using OpenCV functions!

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

cv_sum = cv.add(img1, img2)
np_sum = img1 + img2 # type: ignore

cv.imshow("CV Sum", cv_sum)
cv.imshow("Numpy Sum", np_sum)
cv.waitKey(0)
cv.destroyAllWindows()

