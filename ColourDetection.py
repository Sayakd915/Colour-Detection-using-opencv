import cv2
import numpy as np

# Loading the image
image = cv2.imread('image.jpg')

# Converting the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining the range of red color 
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Defining the range of blue color
lower_blue = np.array([100, 120, 70])
upper_blue = np.array([124, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Defining the range of green color
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Defining the range of yellow color
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Applying the mask to the original image using a bitwise AND operator to extract the parts of the image that correspond to each color range
result_red = cv2.bitwise_and(image, image, mask=mask_red)
result_blue = cv2.bitwise_and(image, image, mask=mask_blue)
result_green = cv2.bitwise_and(image, image, mask=mask_green)
result_yellow = cv2.bitwise_and(image, image, mask=mask_yellow)

# Displaying the original image and the results for each color in separate windows
cv2.imshow('Original Image', image)
cv2.imshow('Red', result_red)
cv2.imshow('Blue', result_blue)
cv2.imshow('Green', result_green)
cv2.imshow('Yellow', result_yellow)

cv2.waitKey(0) # Pressing 0 will close all windows
cv2.destroyAllWindows()
