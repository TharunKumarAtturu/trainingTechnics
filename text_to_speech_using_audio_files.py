''' Text to Speech using audio files. '''
from playsound import playsound 
given_number = input("Enter a number: ")
def get_audio_from_text():
	try:
		[playsound(digit + '.wav') for digit in given_number]

	except Exception as error:
		print("Error!", error)
		print("Text to speech failed!")

get_audio_from_text()
