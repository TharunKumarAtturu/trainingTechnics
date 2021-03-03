''' Text to Speech using audio files. '''
from playsound import playsound 
number_list = []
given_number = input("Enter a number: ")
def text_to_audio():
	try:
		[playsound(digit + '.wav') for digit in given_number]

	except Exception as error:
		print("Error!", error)
		print("Text to speech failed!")

text_to_audio()
