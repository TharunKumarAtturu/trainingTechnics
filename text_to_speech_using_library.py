import pyttsx3
engine = pyttsx3.init()
text = []
given_text = input("Enter a number: ")
for x in given_text:
	text.append(x)
	text.append(" ")

engine.say(text)
engine.runAndWait()
