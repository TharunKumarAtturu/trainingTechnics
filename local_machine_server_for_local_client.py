'''Local machine server for Local client'''
import socket
#Defining a socket object and stream.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binding the connection between this Local server and cilent
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	#Accepting the connection and getting address.
	client_socket, address = s.accept()
	#Printing the confirmation meassage along with address.
	print(f"connection from {address} has been established!")
	#Encoding the message to client.
	client_socket.send(bytes("Welcome to the server!", "utf-8"))
	#Closing the socket connection.
	client_socket.close()
