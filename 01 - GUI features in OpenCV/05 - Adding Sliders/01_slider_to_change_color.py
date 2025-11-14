import numpy as np
import cv2 as cv

def callback(x):
    '''
    Do Nothing
    '''
    pass

HEIGHT = 300
WIDTH = 512
CHANNELS = 3

WINDOW_NAME = 'image'


# Create a window with a black image
cv.namedWindow(WINDOW_NAME)
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)

# Create trackbars for changing the color
# 1st argument : Title of slider
# value : default value
# count : max value
cv.createTrackbar('R', WINDOW_NAME, 0, 255, callback)
cv.createTrackbar('G', WINDOW_NAME, 0, 255, callback)
cv.createTrackbar('B', WINDOW_NAME, 0, 255, callback)


# OpenCV does not have a button functionality by default. We can use
# a trackbar to get such a functionality by setting value=0 and count=1
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, WINDOW_NAME, 0, 1, callback)


while True:
    # Display the window with the image
    cv.imshow(WINDOW_NAME, img)

    # Check for Key Press to exit
    k = cv.waitKey(20) & 0xFF

    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break

    # Get current positions of four trackbars
    r = cv.getTrackbarPos('R', WINDOW_NAME)
    g = cv.getTrackbarPos('G', WINDOW_NAME)
    b = cv.getTrackbarPos('B', WINDOW_NAME)
    s = cv.getTrackbarPos(switch, WINDOW_NAME)

    # Error handling : if the user closes the window by clicking [x] at the window's corner
    # the loop is still running since the termination condition for the loop depends on waitKey
    # As a result, getTrackbarPos will try to access a destroyed window, and return -1
    # To avoid OverflowError, we break the loop if this is detected
    if r < 0 or b < 0 or g < 0:
        break

    # If switch is off, reset the image to black
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

# Cleanup
cv.destroyAllWindows()