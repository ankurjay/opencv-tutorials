import numpy as np
import cv2 as cv

# Load a color image
img = cv.imread("data/messi5.jpg")

# In OpenCV, the img is a numpy array of Rows = HEIGHT and 
# Columns = WIDTH. Indexing is done as img[row][col]. Naturally,
# (row, col) = (y, x) coordinate, unlike cv.rectangle() where 
# the coordinates are provided in (x, y) format.

# ---- Access a pixel value and print it ----

# Access all color channels
px = img[100, 100]
print("Pixel value at (r=100,c=100) : ", px)

# Access only the blue color channel
blue = img[100, 100, 0]
print("Blue color value at (r=100,c=100) : ", blue)

# Modify the full pixel
img[100, 100] = [255, 255, 255] # Set to white
print("Modified pixel value at (r=100, c=100) ", img[100, 100])

# ---- Access Image Properties -------------

print("Shape of the image is : ", img.shape)

# Make a grayscale version to view its shape
gray = img.copy()
gray = cv.cvtColor(gray, cv.COLOR_BGR2GRAY)
print("Shape of the grayscale image is : ", gray.shape)

print("Dtype of the image is : ", img.dtype)

# ---- Access an ROI in the Image ---------

# Region-of-Interest (ROI) is a (usually) rectangular
# region that we can select within the image. This is 
# achieved via numpy indexing. 

# Here, we select an ROI from the image, and copy it
# to another region in the image. Note that this will
# overwrite the values of the original pixels of the
# other region.

ball = img[280:340, 330:390]
cv.imshow("Before Copy", img)
cv.imshow("Ball ROI", ball)
img[273:333, 100:160] = ball
cv.imshow("After copy", img)

# Wait for a key press indefinitely to keep the windows open
cv.waitKey(0)

# Destroy all created windows after the key is pressed
cv.destroyAllWindows()
