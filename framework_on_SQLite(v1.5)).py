import sqlite3
DATABASE_NAME = "framework.db"
MENU_FILE = "menu_for_SQLite.cfg"
TABLE_NAME = "framework_table"
TABLE_NAME_FOR_DELETED = "table_for_deleted_records"
field_names_list = []

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

meta_data = cursor.execute("pragma table_info({})".format(TABLE_NAME))
for field_names in meta_data:
	field_names_list.append(field_names[1])

def print_update_menu():
	'''Prints the Update Menu options.'''
	for counter in range(1, (len(field_names_list))):
		print(str(counter) + ". " + field_names_list[counter])


def insert_a_record():
	'''Add a record to the table.'''
	field_values = []
	[field_values.append(input("Enter the " + field + ": "))for field in field_names_list]
	value = ""
	
	for counter in range(len(field_names_list)):
		if counter != len(field_names_list) - 1:
			value += "?,"
		else:
			value += "?"	
	try:
		cursor.execute("INSERT INTO " + TABLE_NAME + " VALUES(" + value + ")", field_values)
		result = cursor.fetchone()
		connection.commit()
	
	except Exception as error:
		print("Error!" + error)
		connection.commit()
		connection.rollback()
		print("Record insertion failed.")
	
	else:
		print("Record added successfully.")

def show_all_records():
	'''Reads all the records from the current table and print them to the output screen. '''
	try:
		records = connection.execute("SELECT * FROM " + TABLE_NAME)

	except Exception as error:
		print("Error!", error)
		print("Displaying Record failed.")
	else:
		print(field_names_list)
		[print(record) for record in records]



def update_a_record():
	'''Updates the record with help of primary key.'''
	temporary_id = input("Enter " + field_names_list[0] + " to update the record: ")
	print_update_menu()
			
	try:	
		option = int(input("Select one option to update:  "))
		if option > 0 and option < (len(field_names_list)):
			temporary_data =  input("Enter new " + field_names_list[option] + " : ")
			cursor.execute(" UPDATE " + TABLE_NAME + " SET " +  field_names_list[option] + " = ? WHERE " + field_names_list[0] + " = ?", (temporary_data, temporary_id))
			connection.commit()
			# print("number_of_rows affected =", cursor.rowcount)
			result = cursor.rowcount
			
			if result != 0:
				connection.commit()
				print("Record updated successfully.")
	
			elif result == 0:
				print("Error! Invalid " + field_names_list[0] + ": " + temporary_id + "." )
		
		elif option > (len(field_names_list)) and option < 0:
			print("Enter the valid option.")

	except Exception as error:
		print("Error!", error)
		connection.commit()
		connection.rollback()
		print("Update failed.")

def delete_a_record():
	''' Insert the Record into deleted record table and Delete that record from the table.'''
	try:
		temporary_id = input("Enter " + field_names_list[0] + " to delete the record: ")
	# 	cursor.execute("UPDATE " + TABLE_NAME +  "SET " + field_names_list[-1] + "= 0" +" WHERE " + field_names_list[0] + " = " + temporary_id)
		cursor.execute("INSERT  INTO " + TABLE_NAME_FOR_DELETED + " SELECT * FROM " + TABLE_NAME + " WHERE " + field_names_list[0] + " = " + temporary_id)	
		result = cursor.rowcount
		if result != 0:
			connection.commit()
			cursor.execute("DELETE FROM " + TABLE_NAME +" WHERE " + field_names_list[0] + " = " + temporary_id)
			connection.commit()
			print("Record deleted successfully!")

		elif result == 0:
			print("NO Record with " + field_names_list[0] + ": " + temporary_id + ".")
			print("Deleting a record operation failed!")
	
	except Exception as error:
		print("Error!", error)
		connection.commit()
		connection.rollback()
		print("Deleting a record operation failed!")


def search_a_record():
	'''Find and displays that record, if given temporary id matches with the primary key.'''
	try:
		matched_record = []
		temporary_id = input("Enter " + field_names_list[0] + " to find the record: ")
		record_data = connection.execute("SELECT * FROM " + TABLE_NAME + " WHERE " + field_names_list[0] + " = " + temporary_id)
		# print(cursor.rowcount)
		for record in record_data:
			matched_record.append(record)
			
		if matched_record != []:
				print(matched_record)
		
		else:
			print("No Record found with " + field_names_list[0] + ": " + temporary_id) 
	
	except Exception as error:
		print("Error!", error)
		connection.commit()
		connection.rollback()
		print("Search operation failed.")

def exit_from_main_menu():
	'''Exits from main.'''
	print("Thank you.")
	connection.close()
	exit()

def show_main_menu():
	'''Displays the Main menu on the output screen.'''
	while True:
		print(open(MENU_FILE).read())
		[insert_a_record, show_all_records, update_a_record, delete_a_record, search_a_record, exit_from_main_menu][int(input("Enter your option: ")) - 1]()

show_main_menu()	
