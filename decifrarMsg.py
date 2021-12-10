#python3 version
import rsa
print('\\-------------------------------//')
print('**Prj Banco de Dados Distribuidos**')
print('\\-------------------------------//')
print('Decifrador de mensagens')
print('Digite as seguintes informacoes')
#Informar o endereço da chave privada
arqnomepri = input('Endereco da chave privada (c:\chaves\myPri.txt): ')
#Informar o endereço da mensagem a ser decifrada
arqnomemsg = input('Endereco e nome da mensagem a ser decifrada (c:\msg.txt): ')

##Abrir o arquivo com a chave privada
arq = open(arqnomepri,'rb')
##Leitura da chave privada
txt = arq.read()
arq.close()

#decodifico para o formato expoente e modulo
pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')

#abre o arquivo com a msg cifrada
arq = open(arqnomemsg,'rb')

##carrega a msg cifrada
msgc = arq.read()
arq.close()

#decifro a msg passando a chave privada
msg = rsa.decrypt(msgc,pri)

#Exibe no console a mensagem descriptografada
print('Mensagem decifrada: ' + msg.decode('utf-8'))



