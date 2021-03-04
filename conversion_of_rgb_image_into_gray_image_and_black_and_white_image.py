''' Conversion of Original (BGR) Image into Gray Image and Black and White Image.'''

import cv2
IMAGE_FILE_NAME = 'original_image.png'
original_image = cv2.imread(IMAGE_FILE_NAME)
try:
  '''Converts given original (BGR) Image into Gray Image and Balck and White Image.'''
	gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
  
	(thresh, black_and_white_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

except Exception as error:
	print("Error!", error)
	print("Conversion Failed!")


else:
  '''Displays the Original Image (BGR), converted Gray Image and converted Black and Image.'''
	cv2.imshow('Black And White image', black_and_white_image)
	cv2.imshow('Original image',original_image)
	cv2.imshow('Gray image', gray_image)
  
	cv2.waitKey(0)
	cv2.destroyAllWindows()
