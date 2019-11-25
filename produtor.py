import socket
import random

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')

tipo = "prod"
tcp.send (tipo.encode())



print (msg)

while True:
    conteudo = str(random.randint(0,100))
    tcp.send (conteudo.encode())
tcp.close()
