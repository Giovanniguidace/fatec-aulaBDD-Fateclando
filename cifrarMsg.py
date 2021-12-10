#python3 version
import rsa
print('\\-------------------------------//')
print('**Prj Banco de Dados Distribuidos**')
print('\\-------------------------------//')
print('Cifrador de mensagens')
print('Digite as seguintes informacoes')
#Informa a chave pública que será usada para cifrar a mensagem
arqnomepub = input('Endereco da chave publica (c:\chaves\myPub.txt): ')
#A mensagem que será cifrada
msg = input('Mensagem a ser cifrada: ').encode('utf-8')
#Onde o arquivo da mensagem cifrada será salva
arqnomemsg = input('Endereco e nome da mensagem (c:\msg.txt): ')

#Abre o arquivo com o nome definido
arq = open(arqnomepub,'rb')
#Faz a leitura da chave pública
txt = arq.read()
#Fecha o arquivo
arq.close()

#decodifico para o formato expoente e modulo
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

#cifra a mensagem com a chave pública
msgc = rsa.encrypt(msg,pub)

#Salva a mensagem cifrada no arquivo
arq = open(arqnomemsg,'wb')
arq.write(msgc)
arq.close()

print('Mensagem cifrada no arquivo ' + arqnomemsg)



