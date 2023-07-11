import socket


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for _ in range(10):
        s.sendall(b'Hello, World')
        data = s.recv(1024)
        print("Recebido do servidor: ", data)