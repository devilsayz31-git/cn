import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5050))

client.send("Hello Server, this is the TCP Client".encode())

data = client.recv(1024).decode()
print("Server:", data)

client.close()
