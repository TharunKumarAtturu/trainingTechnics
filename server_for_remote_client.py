'''Server for remote client.'''
import socket 
import threading

HEADER = 64
PORT = 1436
FORMAT = "utf-8"
# SERVER = ""165.22.14.77
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	'''Handles the connection betweeen server and client.'''
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] {msg}")
			conn.send("Message received".encode(FORMAT))

	conn.close()




def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")

	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target = handle_client, args = (conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") 

print("[STARTING] server is starting...")
start()