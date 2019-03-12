from game import Game

def main():
	jogo = Game(3 , 1000)
	#jogo.showCardsOnHand()
	jogo.givePlayersCards()
	jogo.showCardsOnHand()
	jogo.Flop()
	jogo.showFlop()
	jogo.Turn()
	jogo.showTurn()
	jogo.River()
	jogo.showRiver()
	jogo.showCardsOnTable()

main()
	
