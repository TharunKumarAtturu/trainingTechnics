'''Client which can connect to Local machine server.'''
import socket
#Creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Establishing the connection between this cilent and Local machine server.
s.connect((socket.gethostname(), 1234))
#Receving the message into a buffer.
message = s.recv(1024)
#Decoding the Encoded message from the server and Displaying the message on output screen.
print(message.decode("utf-8"))
