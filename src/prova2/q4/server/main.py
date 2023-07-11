import socket
import random
from threading import Thread

# for divisível por 4 dizemos que ele é bissexto
# se o ano não terminar em 00
#    Se for 00, verifica se é divisilvel por 400 se sim, é bissexto e contrário, não.

bissexto = lambda ano: (ano % 4 == 0 and str(ano)[-2:] != '00') or (ano % 4 == 0 and str(ano)[-2:] == '00' and ano % 400 == 0)

def verifica(conn, addr):
    while True:
        data = conn.recv(1024)
        print("Recebido do cliente: ", data)
        if not data:
            break
        data = data.decode()
        data = data.split(',')
        ano = int(data[0])
        name = data[1]
        data = f"{name}: {ano} eh SIM um ano bissexto\n" if bissexto(ano) else f"{name}: {ano} NAO eh um ano bissexto\n"
        conn.sendall(data.encode())
    conn.close()


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Cria um socket TCP/IP
    # Toda vez que algum cliente se conectar, será criada uma nova thread
    # para atendê-lo
    s.bind((HOST, PORT)) # Associa o socket a um endereço e porta
    s.listen() # Coloca o socket em modo de escuta

    print("Aguardando conexões...")

    while True:
        conn, addr = s.accept()
        print("Conectado por: ", addr)
        t = Thread(target=verifica, args=(conn, addr)) # Cria uma nova thread para atender o cliente
        t.start() # Inicia a thread




