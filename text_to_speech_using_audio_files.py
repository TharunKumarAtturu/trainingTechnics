''' Text to Speech using audio files. '''
from playsound import playsound 
given_number = input("Enter a number: ")
def convert_text_to_audio(input_string):
	try:
		[playsound(digit + '.wav') for digit in given_number]

	except Exception as error:
		print("Error!", error)
		print("Text to speech failed!")

convert_text_to_audio(given_number)
