'''Text to Speech using library(pyttsx3).'''
import pyttsx3
engine = pyttsx3.init()
text = []
given_text = input("Enter a number: ")
def text_to_speech_using_library():
  try:
    [text.append(x + " ") for x in given_text]
    engine.say(text)
    engine.runAndWait()

  except Exception as error:
	  print("Error!", error)
	  print("Text to speech failed!")
  
text_to_speech_using_library()
