import socket
import random
from threading import Thread

HOST = '127.0.0.1'
PORT = 65432

def enviaAno(s, name):
    s.settimeout(5)  # Tempo máximo de espera para receber uma resposta do servidor
    for _ in range(5):
        s.sendall(f"{random.randint(0, 2023)},{name}".encode())
        try:
            data = s.recv(1024)
        except socket.timeout:
            print(f"Timeout para {name}. Encerrando a thread.")
            break
        if not data:
            break
        print("Recebido do servidor:", data.decode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    thrs = [Thread(target=enviaAno, args=(s, f"T{x}"), name=f"T{x}") for x in range(5)]
    for t in thrs: 
        t.start()
    for t in thrs: 
        t.join()