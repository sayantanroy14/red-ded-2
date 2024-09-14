import cv2

# Assume that you know the length of the rectangle and it is stored in a variable called `known_length`
known_length = 10  # in pixels

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    # Get the frame from the video capture
    _, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in the HSV color space
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)

    # Create a mask for the red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find the contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Iterate over the contours
    for contour in contours:
        # Check if the contour is a rectangle
        if cv2.isContourConvex(contour):
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Check if the rectangle is red
            if mask[y:y+h, x:x+w].all():
                # Calculate the aspect ratio of the rectangle
                aspect_ratio = w / h

                # Calculate the unknown length of the rectangle using the known length and the aspect ratio
                unknown_length = known_length / aspect_ratio

                # Print the unknown length of the rectangle
                print(f'Unknown length: {unknown_length} pixels')

    # Show the frame
    cv2.imshow('Frame', frame)

    # Check if the user pressed the `Esc` key
    if cv2.waitKey(1) == 27:
        break

# Release the video capture and close
