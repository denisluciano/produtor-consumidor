import socket
import time
import random


HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+C\n')

tipo = "cons"
tcp.send (tipo.encode())
contador = 0

while True:
    
    time.sleep(random.uniform(0.5, 3.0))
    tcp.send("ok".encode())
    msg2 = tcp.recv(1024)
    contador += 1
    print("tirou do buffer: ", msg2.decode())
tcp.close()
