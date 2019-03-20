from game import Game
import os
clear = lambda: os.system('cls')

def main():
	jogo = Game()
	while(True):
		QntJogadores = input("Quantidade de jogadores(Máx: 9): \n")
		if(QntJogadores.isalpha() == False and int(QntJogadores) <= 9 and int(QntJogadores) >= 1):
			QntJogadores = int(QntJogadores)
			clear()
			break
		else:
			clear()
			print("Valor inválido.")
	while(True):
		QntMonay = input("Valor das fichas que seram dadas no torneio: \n")
		if(QntMonay.isalpha() == False):
			QntMonay = int(QntMonay)
			clear()
			break
		else:
			clear()
			print("Valor inválido.")
	
	jogo.addPlayers(QntJogadores,QntMonay)
	
	while(True):
		jogo.newGame()
		jogo.givePlayersCards()
		#jogo.betTime()
		jogo.Flop()
		jogo.showFlop()
		#jogo.betTime()
		jogo.Turn()
		jogo.showTurn()
		#jogo.betTime()
		jogo.River()
		jogo.showRiver()
		jogo.showCardsOnTable()
		jogo.showPlayerGame()
		#jogo.betTime()
		jogo.showWinner()

		goOn = input("Mais um jogo? (y/n) \n")
		if(goOn == "n"):
			break
			
		

	

main()
	
	
	
	
	
	
	
	
	
	
	
	
	