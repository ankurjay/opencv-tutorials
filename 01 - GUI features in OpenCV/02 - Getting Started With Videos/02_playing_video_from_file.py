import numpy as np
import cv2 as cv

# Create a VideoCapture object. 
# The constructor takes an argument : device name or name of video file.
# In this case we specify the file name
cap = cv.VideoCapture('data/vtest.avi')


# If the capture could not be initialized for some reason, exit
if not cap.isOpened():
    print("Cannot open camera!")
    exit()


while cap.isOpened():
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

    # Keep showing the frame for 25ms unless 'q' is pressed

    # Use appropriate time for cv.waitKey(). If it is too less,
    # the video playback will be too fast, and if it is too high,
    # the video playback will be too slow. 25ms is OK in most cases.
    if cv.waitKey(25) == ord('q'):
        break

# Release the Capture
cap.release()
cv.destroyAllWindows()