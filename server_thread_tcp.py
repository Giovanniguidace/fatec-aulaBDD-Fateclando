#Servidor TCP
import socket
import rsa
from threading import Thread

global tcp_con

# abre a chave pública
arq = open('/home/gtanuri/Documents/Fatec/5 Semestre/BDD/atividade6/user1Pub.txt','rb')
txt = arq.read()
arq.close()

# abre a chave privada
arqPri = open('/home/gtanuri/Documents/Fatec/5 Semestre/BDD/atividade6/user1Pri.txt','rb')
txtPri = arqPri.read()
arqPri.close()

pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')
pri = rsa.PrivateKey.load_pkcs1(txtPri, format='PEM')

def enviar():
    global tcp_con

    # o servidor passa a mensagem a ser criptografada
    msg = input().encode('utf-8')
    # antes de enviar a mensagem, a chave pública do cliente criptografa a msg.
    msgc = rsa.encrypt(msg,pub)
    while True:
         # a mensagem criptografada é enviada para o cliente
        tcp_con.send(msgc)
        msg = input().encode('utf-8')

# Endereco IP do Servidor
HOST = ''

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        # msg = tcp_con.recv(1024)
        msg = rsa.decrypt(tcp_con.recv(1024),pri)
        # print ("Server:", msg)
        if not msg: break
        print("Cliente Msg criptografada:", tcp_con.recv(1024))
        print("Cliente Msg descriptografada:",msg)
    print ('Finalizando conexao do cliente', cliente)
    tcp_con.close()
