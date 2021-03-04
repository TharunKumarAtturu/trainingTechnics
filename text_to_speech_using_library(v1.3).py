'''Text to Speech using library(pyttsx3).'''
import pyttsx3
engine = pyttsx3.init()
given_number = input("Enter a number: ")

def get_speech_from_given_text_using_library():
  try:
    [engine.say(digit) for digit in given_number]
    engine.runAndWait()

  except Exception as error:
	  print("Error!", error)
	  print("Text to speech failed!")
  
get_speech_from_given_text_using_library():
