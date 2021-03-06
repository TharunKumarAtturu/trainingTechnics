'''Client for remote Server.'''
import socket

HEADER = 64
PORT = 1436
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "1165.22.14.77"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length = send_length + b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))


send("Hello from client!")
input()
send(DISCONNECT_MESSAGE)

