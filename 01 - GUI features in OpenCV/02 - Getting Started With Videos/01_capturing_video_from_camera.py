import numpy as np
import cv2 as cv

# Create a VideoCapture object. 
# The constructor takes an argument : device name or name of video file.
# Use a unique ID for each camera you capture from.
cap = cv.VideoCapture(0)


# If the capture could not be initialized for some reason, exit
if not cap.isOpened():
    print("Cannot open camera!")
    exit()


# The capture was initialized. We can inspect the properties of the video
# using cap.get(prop_id) where prop_id is a number from 0 to 18.
# Each number denotes a property of the video, like frame width, height etc.

default_frame_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
default_frame_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

# Default frame width x height = 640 x 480
print("Default Frame Width : %s, Frame Height : %s" % (default_frame_width, default_frame_height))

# We can modify it using cap.set(prop_id, value)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)


while True:
    # Capture Frame-by-Frame
    # Returns an individual (bool, frame)
    ret, frame = cap.read()

    # If the frame is read correctly, ret is true, and we have frame data.
    # If not, then we need to break the loop.
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Frame is read correctly, so do some operations on it

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)

    # Keep showing the frame for 1ms unless 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        break

# Release the Capture
cap.release()
cv.destroyAllWindows()