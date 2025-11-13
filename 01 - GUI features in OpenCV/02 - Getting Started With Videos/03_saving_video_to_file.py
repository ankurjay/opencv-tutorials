import numpy as np
import cv2 as cv

# Create a VideoCapture object, with the argument = device id
# of the camera from where we are capturing the video, or
# the filename of the file we want to read
cap = cv.VideoCapture(0)

# Define the codec (coder-decoder that compresses and decompresses digital media files)
# FourCC is a 4-byte code used to specify the video codec.
# List of available codes is found at fourcc.org. It is platform-dependent.
codec = cv.VideoWriter.fourcc(*'X264')

# Create a VideoWriter object
out = cv.VideoWriter('/tmp/output.mkv', codec, fps=20, frameSize=(640, 480))


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
    frame = cv.flip(frame, 0)

    # Write the flipped frame
    out.write(frame)

    # Also display the flipped frame in a window
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break


# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
