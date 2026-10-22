import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)

client.sendto("Hello UDP Server, this is the UDP Client".encode(), ("localhost", 5051))

data, addr = client.recvfrom(1024)
print("Server:", data.decode())

client.close()
