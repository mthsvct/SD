import socket

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NO = 6789
Message = "Hello, Server"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

print("Message sent. Waiting for response...")

data, addr = clientSock.recvfrom(1024)
print("Message: ", data, " End. Server:", addr)
