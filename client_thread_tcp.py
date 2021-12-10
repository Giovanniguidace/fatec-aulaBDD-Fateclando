#Cliente TCP
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

def receber():
    global tcp_con
    while True:
        # recebe a mensagem do servidor criptografada, descriptografa a mensagem e exibe no console.
        msg = rsa.decrypt(tcp_con.recv(1024),pri)
        print("Server Msg criptografada:", tcp_con.recv(1024))
        print("Server Msg descriptografada:",msg)

def enviar():
    global tcp_con
    print ('Para sair use CTRL+X\n')

    # o cliente passa a mensagem a ser criptografada
    msg = input().encode('utf-8')
    # antes de enviar a mensagem, a chave pública do servidor criptografa a msg.
    msgc = rsa.encrypt(msg,pub)
    while msg != '\x18':
        # a mensagem criptografada é enviada para o servidor
        tcp_con.send(msgc)
        msg = input().encode('utf-8')
    tcp_con.close()

# Endereco IP do Servidor
SERVER = '127.0.0.1'

# Porta que o Servidor esta escutando
PORT = 5002

tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp_con.connect(dest)


t_rec = Thread(target=receber, args=())
t_rec.start()

t_env = Thread(target=enviar, args=())
t_env.start()
