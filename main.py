from game import Game

def main():
	jogo = Game(2 , 1000)
	jogo.givePlayersCards()
	jogo.showCardsOnHand()
	jogo.Flop()
	jogo.showFlop()
	jogo.Turn()
	jogo.showTurn()
	jogo.River()
	jogo.showRiver()
	jogo.showCardsOnTable()
	jogo.showPlayerGame()

	

main()
