import socket
import random
import select

contador = 0
inn = 0
out = 0
lugares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vezes = 0


HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)


# Aguardando as duas conexoes do produtor e 
# consumidor serem estabelecidas
for _ in range(0,2):
    con, cliente = tcp.accept()
    if con.recv(4).decode() == 'prod':
        print ('Concetado pelo produtor: ', cliente)
        prod=con
    else:
        print ('Concetado pelo consumidor: ', cliente)
        cons=con
    
  
inputs=[prod,cons]


while vezes < 100:
    # Parcialmente cheio
    if contador > 0 and contador < 10:
        print("entrou aqui dentro")
        entrada,_,erro=select.select(inputs, [], inputs)
        con = entrada[random.randint(0,len(entrada)-1)]
        msg = con.recv(1024).decode()

        print (lugares)
        print (vezes)

        if con is prod:
            print("produtor em açao \n")
            
            if not msg: break
            lugares[(inn % 10)] = msg
            prod.send("ok".encode())
            inn += 1
            contador += 1


        if con is cons:
            print("consumidor em açao \n")
            
            msgSend = lugares[out % 10]
            lugares[out % 10] = 0
            cons.send(msgSend.encode())
            out += 1
            contador -= 1
            
            
    # Cheio ou vazio
    else:
        entrada,_,erro=select.select(inputs, [], inputs)
        con = entrada[random.randint(0,len(entrada)-1)]
        msg = con.recv(1024).decode()
        
        if contador == 0: #buffer vazio
            if con is prod:
                print("ta vazio \n")
                
                if not msg: break
                lugares[(inn % 10)] = msg
                prod.send("ok".encode())
                inn += 1
                contador += 1
            else:
                cons.send("buffer vazio".encode())
        else: #buffer cheio
            if con is cons:
                print("ta cheio \n")
                
                msgSend = lugares[out % 10]
                lugares[out % 10] = 0
                cons.send(msgSend.encode())
                out += 1
                contador -= 1
            else:
                prod.send("buffer cheio".encode())

    vezes += 1


print ('Finalizando conexao do cliente')
prod.close()
cons.close()
