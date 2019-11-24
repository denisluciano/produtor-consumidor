import socket
import random
import select

contador = 1
inn = 1
out = 1
lugares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


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



while True:

    while contador < 100:
        # Parcialmente cheio
        if contador > 0 and contador < 1000:
            print("entrou aqui dentro")
            entrada,_,erro=select.select(inputs, [], inputs)
            con = entrada[random.randint(0,len(entrada)-1)]
            msg = con.recv(1024)
            print("passou select e con : ")
            print(con)

            if con is prod:
                print("produtor em açao", end = '')
                if not msg: break
                print("mensagem produtor: ", msg, end = '')

            if con is cons:
                print("consumidor em açao", end = '')
                if not msg: break
                print("mensagem consumidor: ", msg, end = '')
        # Cheio ou vazio
        else:
            if contador == 0: #buffer vazio
                print("ta vazio")
            else: #buffer cheio
                print("ta cheio")

        contador += 1


    print ('Finalizando conexao do cliente', cliente)
    con.close()
