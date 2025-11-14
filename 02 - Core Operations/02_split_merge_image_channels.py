import numpy as np
import cv2 as cv

# Load a color image
img = cv.imread("data/messi5.jpg")


# ---------- Splitting and Merging channels -------

# Sometimes you need to work separately on the B,G,R channels
# of an image. You can use cv.split() to do this.
b, g, r = cv.split(img)

# Each split channel will have ROWS x COLS size.

# You can merge back the channels using cv.merge()
img = cv.merge((b, g, r))


# --------- Using Numpy Indexing to access channels ---

blue = img[:, :, 0]
print("Shape of blue channel : ", blue.shape)

# cv.split() is an expensive operation, so we use it only
# when necessary. For simple operations, we can use numpy
# indexing.

# For example. set all red pixels to zero
cv.imshow("Before setting R=0", img)
img[:, :, 2] = 0
cv.imshow("After setting R=0", img)

cv.waitKey(0)
cv.destroyAllWindows()