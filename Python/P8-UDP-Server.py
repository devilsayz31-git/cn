import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 5051))
print("UDP Server is waiting on port 5051...")

data, addr = server.recvfrom(1024)
print("Client", addr, ":", data.decode())

server.sendto("Hello from UDP Server (no connection needed)".encode(), addr)

server.close()
