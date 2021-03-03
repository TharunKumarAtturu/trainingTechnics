'''Text to S '''
import pyttsx3
engine = pyttsx3.init()
text = []
given_text = input("Enter a number: ")
[text.append(x + " ") for x in given_text]
engine.say(text)
engine.runAndWait()
