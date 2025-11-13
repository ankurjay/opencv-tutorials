import numpy as np
import cv2 as cv


HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3 # Blue, Green, Red (BGR).

COLOR_BLUE = (255, 0, 0)

WINDOW_NAME = 'image'

# Create a mouse callback function
# This has a specific format (args) but we can define the
# function any way we want
def mouse_callback(event, x, y, flags, params):

    # If the mouse event that triggered this callback was a 
    # double-click of the mouse-left button
    if event == cv.EVENT_LBUTTONDBLCLK:

        # Draw a circle
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


    # Put some text telling the user to press Q or Esc to Exit the program.
    # Always draw this text last so that it appears on top of anything drawn in the window
    font = cv.FONT_HERSHEY_SIMPLEX
    text_data = "Press 'q' or 'Esc' to exit"

    # Draw a thicker, black outline
    cv.putText(img, text=text_data, org=(20,10), fontFace=font, fontScale=0.5, color=(0,0,0), thickness=2, lineType=cv.LINE_AA)
    # Draw the colored text inside that outline
    cv.putText(img, text=text_data, org=(20,10), fontFace=font, fontScale=0.5, color=COLOR_BLUE, thickness=1, lineType=cv.LINE_AA)


# Create a black image
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)

# Create a Window inside which we will display the image, and also capture mouse callbacks
cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, mouse_callback)

# Display the image 
while True:
    cv.imshow(WINDOW_NAME, img)


    # Check for a key-press to detect if we need to close the window

    # cv.waitKey() can return 32-bit or 64-bit integer depending on the architecture
    # This integer can contain additional 'flag' bits in the higher positions 
    # We only care about the last 8 bits, so we do an AND operation with 0xFF
    # This ensures that all bits before the last 8 bits are set to 0.
    k = cv.waitKey(20) & 0xFF

    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break

# Cleanup
cv.destroyAllWindows()