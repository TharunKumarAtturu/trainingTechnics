''' Conversion of Original (BGR) Image into Gray Image and Black and White Image.'''
import cv2
IMAGE_FILE_NAME = input("Enter the Image file name: ")

def convert_original_image_into_grey_image_and_black_and_white_image(input_image_file_name):

	try:
		'''Converts given image into gray image and balck and white image.'''
		original_image = cv2.imread(IMAGE_FILE_NAME + ".png")
		gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

		(thresh, black_and_white_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

	except Exception as error:
		print("Error!", error)
		print("Conversion Failed!")


	else:
		'''Displays the original image, converted gray image and converted black and image/'''
		cv2.imshow('Black And White image', black_and_white_image)
		cv2.imshow('Original image',original_image)
		cv2.imshow('Gray image', gray_image)
	
		cv2.waitKey(0)
		cv2.destroyAllWindows()

convert_original_image_into_grey_image_and_black_and_white_image(IMAGE_FILE_NAME)

