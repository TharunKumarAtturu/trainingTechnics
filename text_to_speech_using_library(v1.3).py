'''Text to Speech using library(pyttsx3).'''
import pyttsx3
audio = pyttsx3.init()
given_number = input("Enter a number: ")

def convert_text_to_audio_using_library(input_string):
  try:
    [audio.say(digit) for digit in given_number]
    audio.runAndWait()

  except Exception as error:
	  print("Error!", error)
	  print("Text to speech failed!")
  
convert_text_to_audio_using_library(given_number)
