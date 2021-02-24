# Framework to perform create and read operation(using lists to store the data).
FIELDS_FILE = 'fields.cfg'
MENU_FILE = 'menu.cfg'
DATA_FILE = 'data.dat'
records = []

def store_temporary_record_list():
	""" Storing the existing data before overwrite records into data file."""
	with open(DATA_FILE, "r") as temp_lists:
		temp_records = temp_lists.read()
		temp_list_from_data_file = eval(temp_records)
		for line in temp_list_from_data_file:
			records.append(line)

with open(FIELDS_FILE, "r") as fields_file:
	fields_list = fields_file.read()
fields = eval(fields_list)

with open(MENU_FILE, "r") as menu_file:
	menu_list = menu_file.read()
menu_lines = eval(menu_list)

def create_record():
	"""Create a record corresponding to fields."""
	with open(DATA_FILE, "w") as data_file:
		record_temp = []
		for field in fields:
			record_temp.append(input("Enter the " + field + ": "))
		records.append(record_temp)
		data_file.write(str(records))

def read_records():
	"""Displays all the records in data file."""
	for field in fields:
		print(field, end = " ")
	print("\n")
	with open(DATA_FILE, "r") as data_file:
		records = data_file.read()
		temp_records = eval(records)
		for lines in temp_records:
			for line in lines:
				print(line, end = " ",)

			print("\n")	

def exit_from_menu():
	"""Exit from the Main Menu."""
	print("Thank you.")
	exit()

def show_main_menu():
	"""Open's the menu file and displays the Main Menu."""
	while True:
		for menu_line in menu_lines:
			print(menu_line)
		[create_record, read_records, exit_from_menu][int(input("Enter your option: ")) - 1]()

store_temporary_record_list()
show_main_menu()
