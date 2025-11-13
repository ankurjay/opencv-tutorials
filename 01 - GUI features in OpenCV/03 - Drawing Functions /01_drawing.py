import numpy as np
import cv2 as cv

# OpenCV treats images as numpy arrays.

'''
Origin
(0,0) ----------------> (WIDTH, 0)
  |
  |
  |
  |
  |
  |
  |
  V
(0, HEIGHT)
'''


HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3 # Blue, Green, Red (BGR).

COLOR_BLUE = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (0, 0, 255)
COLOR_YELLOW = (0, 255, 255)
COLOR_WHITE = (255, 255, 255) 

# Each pixel has 3 channels. If the value of all channels is 0, the pixel is black (no intensity)

# Create a black image. The dtype is uint8, or 8-bit color
# This means that the intensity of each channel takes a value between 0-255
# 0 = no intensity, 255 = max intensity
img = np.zeros((HEIGHT, WIDTH, CHANNELS), dtype=np.uint8)

# ------ Draw a Line ---------

cv.line(img,  pt1=(0,0), pt2=(511,511), color=COLOR_BLUE, thickness=5)


# ------ Draw a Rectangle ----

# pt1 = top-left corner, pt2 = bottom-right corner
cv.rectangle(img,  pt1=(384, 0),  pt2=(510, 128), color=COLOR_GREEN, thickness=3)


#------- Draw a Circle -------

# Negative thickness means draw a Filled Circle
cv.circle(img,  center=(447, 63), radius=63, color=COLOR_RED, thickness=-1)


# ------ Draw an Ellipse -----

MAJOR_AXIS = 100 # pixels
MINOR_AXIS = 50 # pixels
# angle : Angle of rotation of major axis of ellipse in CCW direction about its center point
# startAngle & endAngle : Starting and Ending of ellipse arc, measured in CW direction from major axis
# startAngle = 0 & endAngle = 360 means draw the full ellipse.
cv.ellipse(img, center=(256, 256), axes=(MAJOR_AXIS, MINOR_AXIS), angle=45, startAngle=15, endAngle=220, color=COLOR_WHITE, thickness=-1)


#------- Draw a Polygon ------

vertices = np.array([
    [10, 5],
    [20, 30],
    [70, 20],
    [50, 10]
], dtype=np.int32)

# The np array of vertices needs to be reshaped to ROWS x 1 x 2
# ROWS = number of vertices
# Using '-1' means 'infer the dimension'. Only one dimension can be inferred.
vertices = vertices.reshape((-1, 1, 2)) 

# cv.polylines can draw multiple polylines in one call; it takes a list of arrays of vertices as input
# isClosed = True : The last vertex is connected to the first; you get a closed shape
# isClosed = False : The last vertex is not connected to the first
cv.polylines(img, [vertices], isClosed=True, color=COLOR_YELLOW)


#------- Add Text to Images --------

font = cv.FONT_HERSHEY_SIMPLEX
text_data = "OpenCV"
cv.putText(img, text=text_data, org=(10,500), fontFace=font, fontScale=4, color=COLOR_WHITE, thickness=2, lineType=cv.LINE_AA)


#------- Display the Final Image ---

cv.imshow("Display Window", img)


# Display the image until a key is pressed, or the timer (milliseconds)
# runs out. '0' means wait indefinitely for a key press.
k = cv.waitKey(0)
