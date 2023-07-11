import socket
import random

UDP_IP_ADRESS = "127.0.0.1"
UDP_PORT_NO = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADRESS, UDP_PORT_NO))

print("Server listening...")

while True:
    data, addr = serverSock.recvfrom(1024)
    data = data.decode()
    # Concatenar data com um número aleatório
    data = data + " - " + str(random.randint(0, 100))
    print("Message: ", data, " End. Client:", addr)
    serverSock.sendto(data.encode(), addr)
