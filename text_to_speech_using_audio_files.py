''' Text to Speech using audio files. '''
from playsound import playsound 
number_list = []
given_number = input("Enter a number: ")
def text_to_audio():
	try:
		for x in given_number:
			number_list.append(x)
		for number in number_list:
			playsound( number + ".wav") 

	except Exception as error:
		print("Error!", error)
		print("Text to speech failed!")

text_to_audio()
