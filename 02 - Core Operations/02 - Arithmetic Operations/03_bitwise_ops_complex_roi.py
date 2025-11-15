import numpy as np
import cv2 as cv

img1 = cv.imread('../data/messi5.jpg')
img2 = cv.imread('../data/opencv-logo-white.png')

# We want to put the logo on the top-left corner. 
# Create a generic (rectangular) ROI representing
# the bounding box for this
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
cv.imshow("ROI on Img1", roi)


# Create a mask of the logo

# First, convert to grayscale
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Thresholding will give a matrix of 0 and 255 (max val)
# If the grayscale image's pixel intensity was above
# the threshold, it was set to 255
# This means that colored regions of the logo are 255 (White)
# and the background is 0 (black)
retval, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
cv.imshow("MASK of Img2", mask)

# We also create the inverse mask
mask_inv = cv.bitwise_not(mask)
cv.imshow("Inverse MASK of Img2", mask_inv)



# Now that the inverse mask is created, we want to blackout
# the ROI corresponding to this inverse mask. This means
# that the pixels corresponding to where the logo will
# lie, are now set to 0 / Black.

# Note that we aren't doing a bitwise_and of roi and mask_inv
# Instead, we are doing bitwise_and of the roi with itself
# and applying the mask so that the AND operations are only done on
# select pixels. This is the recommended method to do this,
# mainly because you can't bitwise_and a grayscale and color
# image due to shape mismatch. 
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
cv.imshow("Apply Inverse MASK of Img2 on ROI", img1_bg)


# Take only the region of the logo, from the logo image
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
cv.imshow("Apply MASK of Img2 on itself", img2_fg)

# Add the two
dst = cv.add(img1_bg, img2_fg)
cv.imshow("Add Img1_BG and Img2_FG", dst)

# Now paste the updated region into the image
img1[0:rows, 0:cols] = dst

# Display the final image
cv.imshow("Final Image", img1)



# Wait indefinitely for a keypress to close all display windows
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()
