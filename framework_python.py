# Framework to perform create and read operation(using lists to store the data).
import os
FIELDS_FILE = 'fields.cfg'
MENU_FILE = 'menu.cfg'
DATA_FILE = 'data.dat'
records = []
fields = eval(open(FIELDS_FILE).read())

def store_temporary_record_list():
	""" checking whether the data file is empty,
	    if empty instering a empty list,
	    if not storing the records it in a list. """
	if os.stat(DATA_FILE).st_size == 0:
		empty_list = []
		with open(DATA_FILE, "a") as file_data:
			file_data.write(str(empty_list))
		# eval(open(DATA_FILE, "w").write(str(empty_list)))

	else:
		[records.append(line) for line in eval(open(DATA_FILE).read())]

def create_record():
	"""Create a record corresponding to fields."""
	record_temp = []
	[record_temp.append(input("Enter the "+ field + ": ")) for field in fields]
	records.append(record_temp)
	with open(DATA_FILE, "w") as data_file:
		data_file.write(str(records))

def read_records():
	"""Displays all the records in data file."""
	for field in fields:
		print(field, end = " ")
	print("\n")
	temp_records = eval(open(DATA_FILE, "r").read())
	for lines in temp_records:
			for line in lines:
				print(line, end = " ")
			print("\n")

def exit_from_menu():
	"""Exit from the Main Menu."""
	print("Thank you.")
	exit()

def show_main_menu():
	"""Open's the menu file and displays the Main Menu."""
	while True:
		# print("\n")
		print(open(MENU_FILE).read())
		[create_record, read_records, exit_from_menu][int(input("Enter your option: ")) - 1]()

store_temporary_record_list()
show_main_menu()
