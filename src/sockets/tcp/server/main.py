import socket
import random

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Cria um socket TCP/IP
    s.bind((HOST, PORT)) # Associa o socket a um endereço e porta
    s.listen() # Coloca o socket em modo de escuta
    conn, addr = s.accept() # Aceita uma conexão
    with conn: # Fecha a conexão quando o bloco with terminar
        print("Conectado com ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            data = data.decode()
            # Concatenar data com um número aleatório
            data = data + " - " + str(random.randint(0, 100))
            conn.sendall(data.encode())