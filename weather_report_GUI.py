''' Getting the weather detials of a given city from a GUI window and displaying that weather details on a GUI window '''
from tkinter import *
import requests, json

window = Tk()
window.geometry("400x400")
window.title("Weather Report")
window.configure(bg="#50514F")
window.iconbitmap('weatherIcon.png')

def get_weather_report():
	try:
		city_name = input_city.get()

		response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=794466004f7baef6a081aeefce29c4fb&units=metric')
		total_response = response.json()

		if total_response["cod"] != "404":
			main_from_total_response = total_response["main"]

			current_temperature = main_from_total_response["temp"] 
			current_pressure = main_from_total_response ["pressure"]
			current_humidiy = main_from_total_response["humidity"]

			city_label.config(text = city_name)
			temperature_label.config(text = "Temperature: " + str(current_temperature) + chr(176) + "C")
			pressure_label.config(text = "Pressure: " + str(current_pressure) + "hPa")
			humidity_label.config(text = "Humidity: " + str(current_humidiy) + "%")
		
		else:
			("city Not Found!")

	except Exception as error:

		city_label.config(text = ("Error!", error))
		
# tkinter intry box and label creation
input_city = Entry(window, width='15', font=('Roboto', 15))
input_city.grid(row = 0, column = 1)
button = Button(window, text = "Go", command = get_weather_report)
button.grid(row = 0, column = 5)
# input_city.bind('<Return>', get_weather_report)
# input_city.grid(row = 0, column = 1)
label1 = Label(window, text = "Enter the city Name: ", fg = "white", bg = "#50514F")
label1.grid(row = 0, column = 0)

city_label = Label(font = ("Raleway-MediumItalic", 15),background = "#50514F", foreground = "#F6E8EA")
city_label.grid(row = 1, column = 1) 

temperature_label = Label(font = ("Raleway-MediumItalic", 15), background = "#50514F", foreground = "#F6E8EA")
temperature_label.grid(row = 2, column = 1)

humidity_label = Label(font = ("Raleway-MediumItalic", 15), background = "#50514F", foreground = "#F6E8EA")
humidity_label.grid(row = 3, column = 1)

pressure_label = Label(font = ("Raleway-MediumItalic", 15), background = "#50514F", foreground = "#F6E8EA")
pressure_label.grid(row = 4, column = 1)

mainloop()
