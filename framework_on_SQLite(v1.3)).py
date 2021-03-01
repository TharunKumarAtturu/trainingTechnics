''' Framework to perform CURDS operation for a existing Table in a Existing Database.'''
import sqlite3
DATABASE_NAME = "framework.db"
MENU_FILE = "menu_for_SQLite.cfg"
TABLE_NAME = "sample_table"
field_names_list = []

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()
meta_data = cursor.execute("pragma table_info({})".format(TABLE_NAME))
for field_names in meta_data:
	field_names_list.append(field_names[1])

def print_update_menu():
	'''Prints the Update Menu options.'''
	for counter in range(1, len(field_names_list)):
		print(str(counter) + ". " + field_names_list[counter])

def insert_a_record():
	'''Add a record to the table.'''
	field_values = []
	[field_values.append(input("Enter the " + field + ": "))for field in field_names_list]
	value = ""
	for counter in range(len(field_names_list)):
		if counter != len(field_names_list) - 1:
			value = value + "?,"
		else:
			value = value + "?"	

	cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES(" + value + ")", field_values)
	connection.commit()
	print("Record added successfully.")

def show_all_records():
	'''read's all the records and print them to the output screen. '''
	records = connection.execute("SELECT * FROM " + TABLE_NAME)
	print(field_names_list)
	[print(record) for record in records]

def update_a_record():
	'''Updates the record with help of primary key.'''
	flag = 0
  temporary_id = input("Enter " + field_names_list[0] + " to update the record: ")
	records = cursor.execute("SELECT * FROM " + TABLE_NAME)	
	for record in records:
		if record[0] == temporary_id:
			print_update_menu()
			option = int(input("Enter a option: "))
			field_values = input("Enter " + field_names_list[option] + " to be updated: ")
			cursor.execute("UPDATE " + TABLE_NAME + " SET " + field_names_list[option] + " = ? WHERE " + field_names_list[0] + " = ?", (field_values, temporary_id))
			connection.commit()
      flag = flag + 1
			print("Record updated successfully.")
    
	if (flag == 0):
		print("Error! Invalid " + field_names_list[0] + ": " + temporary_id + "." )

def delete_a_record():
	'''Deletes a record from the table.'''
	temporary_id = input("Enter " + field_names_list[0] + " to delete the record: ")
	records = cursor.execute("SELECT * FROM " + TABLE_NAME)
	for record in records:
		if record[0] == temporary_id:
			cursor.execute("DELETE FROM " + TABLE_NAME +" WHERE " + field_names_list[0] + " = " + temporary_id)
			connection.commit()
			print("Record deleted successfully!")

def search_a_record():
	'''Find and display's then record, if given temporary id matches with the primary key.'''
	matched_record = []
	temporary_id = input("Enter " + field_names_list[0] + " to find the record: ")
	record_data = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + field_names_list[0] + " = " + temporary_id)
	for record in record_data:
		matched_record.append(record)
		print(matched_record)
	if matched_record == []:
		print("No Record found with " + field_names_list[0] + ": " + temporary_id) 

def exit_from_main_menu():
	'''Exit's from program.'''
	print("Thank you.")
	connection.close()
	exit()

def show_main_menu():
	'''Display's the Main menu on the output screen.'''
	while True:
		print(open(MENU_FILE).read())
		[insert_a_record, show_all_records, update_a_record, delete_a_record, search_a_record, exit_from_main_menu][int(input("Enter your option: ")) - 1]()

show_main_menu()	
