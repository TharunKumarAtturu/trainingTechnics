'''Text to Speech using library(pyttsx3).'''
import pyttsx3
engine = pyttsx3.init()
number = []
given_number = input("Enter a number: ")
def text_to_speech_using_library():
  try:
    [number.append(digit + " ") for digit in given_number]
    engine.say(number)
    engine.runAndWait()

  except Exception as error:
	  print("Error!", error)
	  print("Text to speech failed!")
  
text_to_speech_using_library()
