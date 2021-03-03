from playsound import playsound 
number_list = []
given_number = input("Enter a number: ")

for x in given_number :
	number_list.append(x)

for number in number_list:
	playsound( number + ".wav") 


# import pyttsx3
# engine = pyttsx3.init()
# text = "1 2 3 4"
# engine.say(text)
# engine.runAndWait()