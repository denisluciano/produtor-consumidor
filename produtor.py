import socket
import time
import random

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')

tipo = "prod"
tcp.send (tipo.encode())


while True:
    time.sleep(random.uniform(0.5, 3.0))
    conteudo = str(random.randint(1,100))
    print("produziu: ", conteudo)
    tcp.send (conteudo.encode())
    
    msg2 = tcp.recv(1024)
    print("tirou do buffer: ", msg2.decode())
tcp.close()
