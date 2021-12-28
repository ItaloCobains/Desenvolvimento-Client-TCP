import socket
import sys
#lib sys fornece acesso a algumas variaveis e funçoes do interpretador

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		#AF_INET = usar protocolo ip, SOCK_STREAM = para conectação tpc, 0 = tpc
 
	except socket.error as e:
		print('[*]A conexão falhou!!!')
		print(f'[*]ERRO: {e}')
		sys.exit()

	print("[*]Socket criado com sucesso.")
	
	HostAlvo = input('[*]Host or IP: ')
	PortAlvo = int(input('[*]Port: '))
	
	try:
		s.connect((HostAlvo, int(PortAlvo)))
		print(f'[*]CLIENTE TCP CONECTADO COM SUCESSO NO HOST: {HostAlvo} NA PORTA: {PortAlvo}')
		#Vai ficar 2 segundo conectado e depois vai disconectar
		s.shutdown(2)
	except socket.error as e:
		print(f'[*]A CONECÇÃO COM O HOST: {HostAlvo} NA PORTA: {PortAlvo} NÃO FOI POSSIVEL')
		print(f'Erro: {e}')
		sys.exit()

if __name__ == "__main__":
	main()

