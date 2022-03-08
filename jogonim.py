def computador_escolhe_jogada(n, m):
	proximaJogada = False
	i = 1
	while i <= m and not proximaJogada:
		if (n - i) % (m + 1) == 0:
			proximaJogada = True
		else:
			i += 1
	return i

def usuario_escolhe_jogada(n, m):
	jogadorTira = int(input("Quantas peças você vai tirar? "))

	while jogadorTira > m or jogadorTira > n or jogadorTira <= 0:
		print("\nOops! Jogada inválida! Tente de novo.\n")
		jogadorTira = int(input("Quantas peças você vai tirar? "))
	return jogadorTira

def campeonato():
	print("\nVoce escolheu um campeonato!\n")
	i = 1
	pontosComputador = 0
	pontosUsuario = 0
	while i <= 3:
		print(f"**** Rodada {i} ****\n")
		perdedor = partida()
		if perdedor == 0:
			pontosComputador += 1
		else:
			pontosUsuario += 1
		i += 1

	print("**** Final do campeonato! ****\n")
	print(f"Placar: Você {pontosUsuario} X {pontosComputador} Computador")

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	if n % (m + 1) == 0:
		print("\nVoce começa!\n")
		proximo = 0

	else:
		print("\nComputador começa!\n")
		proximo = 1

	while n >= 1:
		if proximo == 1:
			jogadaComputador = computador_escolhe_jogada(n, m)
			if jogadaComputador == 1:
				print("O computador tirou uma peça.")
			else:
				print("O computador tirou", jogadaComputador, "peças.")
			n = n - jogadaComputador
			proximo = 0
		else:
			jogadaUsuario = usuario_escolhe_jogada(n, m)
			if jogadaUsuario == 1:
				print("\nVocê tirou uma peça.")
			else:
				print("\nVoce tirou", jogadaUsuario, "peças.")
			n = n - jogadaUsuario
			proximo = 1
		if n == 1:
			print("Agora resta apenas uma peça no tabuleiro.\n")
		elif n > 1:
			print("Agora restam", n, "peças no tabuleiro.\n")

	if proximo == 0:
		print("Fim do jogo! O computador ganhou!\n")
	else:
		print("Fim do jogo! Você ganhou!\n")
	return proximo

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
tipoJogo = int(input("2 - para jogar um campeonato "))

if tipoJogo == 1:
	partida()
elif tipoJogo == 2:
	campeonato()
