import sys

# Import the OpenCV Library
import cv2 as cv

# Read the image into a numpy array
img = cv.imread("data/starry_night.jpg")


# Check if the image was loaded correctly
if img is None:
    sys.exit("Could not read the image!")


# Display the image. "Display Window" is the window title.
cv.imshow("Display Window", img)


# Display the image until a key is pressed, or the timer (milliseconds)
# runs out. '0' means wait indefinitely for a key press.
k = cv.waitKey(0)

# If the key pressed was 's', save the image.
if k == ord("s"):
    cv.imwrite("/tmp/starry_night.png", img)