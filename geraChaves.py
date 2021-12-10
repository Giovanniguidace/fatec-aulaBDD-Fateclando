#python3 version
import rsa
print ('\\-------------------------------//')
print (' **Prj Banco de Dados Distribuidos**')
print (' \\-------------------------------//')
print ('Gerador de chaves assimetricas')
print ('Digite as seguintes informacoes')
size = input('Tamanho da chave: ')
#Passa um tamanho na base 2 para geração da chave
end = input('Endereco do arquivo (c:\chaves\): ')
#Local onde vai ser salvo as chaves
nome = input('Nome do arquivo: ')
#Nome dos arquivos das chaves

#Utiliza-se a biblioteca RSA para geração das chaves com o tamanho informado
(pub,pri) = rsa.newkeys(int(size))

##cria o arquivo com a chave publica gerada
arqnomepub = end + nome + 'Pub.txt'

#codifico o exponente e modulo da chave para o formate PEM
arq = open(arqnomepub,'wb')
#Escreve a chave pública no arquivo
arq.write(pub.save_pkcs1(format='PEM'))
#Fecha o arquivo da chave pública
arq.close()

##cria o arquivo com a chave privada gerada
arqnomepri = end + nome + 'Pri.txt' 
arq = open(arqnomepri,'wb')
#Escreve a chave pública no arquivo
arq.write(pri.save_pkcs1(format='PEM'))
#Fecha o arquivo da chave privada
arq.close()

print ('Chaves geradas com sucesso')
print (arqnomepub)
print (arqnomepri)






