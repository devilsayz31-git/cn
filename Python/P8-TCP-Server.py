import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 5050))
server.listen(1)
print("TCP Server is waiting for connection on port 5050...")

conn, addr = server.accept()
print("Connected by:", addr)

data = conn.recv(1024).decode()
print("Client:", data)

conn.send("Hello Varad, message received by TCP Server".encode())

conn.close()
server.close()
print("Connection closed.")
