import cv2
import numpy as np

# Initialize VideoCapture
cap = cv2.VideoCapture(0)

# Define color ranges
blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])
green_lower = np.array([35, 70, 70])
green_upper = np.array([85, 255, 255])

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for blue and green colors
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)

    # Apply masks to the frame
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green_result = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Display frames
    cv2.imshow('Frame', frame)
    cv2.imshow('Blue Mask', blue_mask)
    cv2.imshow('Blue Result', blue_result)
    cv2.imshow('Green Mask', green_mask)
    cv2.imshow('Green Result', green_result)

    # Break the loop if 'Esc' is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the VideoCapture and close all windows
cap.release()
cv2.destroyAllWindows()
