import numpy as np 
import cv2 as cv

drawing = False # True if mouse button is pressed
mode = True # if True, draw rectangle, else draw Circle. Press 'm' to toggle modes.

HEIGHT = 512 # pixels
WIDTH = 512 # pixels
CHANNELS = 3 # Blue, Green, Red (BGR).
COLOR_BLUE = (255, 0, 0)
WINDOW_NAME = 'image'

ix, iy = -1, -1

def render_helptext():
    '''
    Render some text telling the user to press 'q' or Esc to Exit the program, or press 'm' to change mode.
    Also display the current drawing mode (Rectangle or Circle)
    '''
    font = cv.FONT_HERSHEY_SIMPLEX
    modestr = "Rectangle" if mode else "Circle"
    text_data = ["Press 'q' or 'Esc' to exit.", "Press 'm' to switch between Rectangle and Circle", "Current mode : " + modestr ]

    # Draw a black backdrop rectangle for text
    cv.rectangle(img, (0, 0), (WIDTH, 40), color=(0,0,0), thickness=-1)
    
    for i in range(len(text_data)):
        # Draw the colored text inside that backdrop
        cv.putText(img, text=text_data[i], org=(10, 10*i + 10), fontFace=font, fontScale=0.5, color=COLOR_BLUE, thickness=1, lineType=cv.LINE_AA)


# Create a mouse callback function
# This has a specific format (args) but we can define the
# function any way we want
def mouse_callback(event, x, y, flags, params):

    global ix, iy, drawing, mode, temp_image

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        # If Button was pressed while the mouse was moving
        if drawing == True:

            # Create a temporary copy of the original image to draw the current shape
            temp_image = img.copy()

            # Rectangle mode
            if mode == True:
                cv.rectangle(temp_image, (ix, iy), (x, y), COLOR_BLUE, 1)
            else:
                cv.circle(temp_image, (x,y), 5, COLOR_BLUE, 1)

            # Display the temporary image
            cv.imshow(WINDOW_NAME, temp_image)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), COLOR_BLUE, 1)
        else:
            cv.circle(img, (x,y), 5, COLOR_BLUE, 1)

        # Display the updated main image
        cv.imshow(WINDOW_NAME, img)
    
    render_helptext()



# Create a black image
img = np.zeros((HEIGHT, WIDTH, CHANNELS), np.uint8)
temp_image = img.copy()

# Create a Window inside which we will display the image, and also capture mouse callbacks
cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, mouse_callback)

while True:
    # The callback is handling imshow() so we don't need to write it here.

    # Check for a key-press to detect if we need to close the window or change mode

    # cv.waitKey() can return 32-bit or 64-bit integer depending on the architecture
    # This integer can contain additional 'flag' bits in the higher positions 
    # We only care about the last 8 bits, so we do an AND operation with 0xFF
    # This ensures that all bits before the last 8 bits are set to 0.
    k = cv.waitKey(20) & 0xFF

    if k == ord('m'):
        mode = not mode
        # Once the mode has changed, we need to update the help text
        # and re-render the image. If we don't call imshow() here,
        # the mode change won't be reflected until the next mouse event.
        render_helptext()
        cv.imshow(WINDOW_NAME, img)


    # 27 is the ASCII code for ESC key
    if k == ord('q') or k == 27:
        break

# Cleanup
cv.destroyAllWindows()