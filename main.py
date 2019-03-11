from game import Game

def main():
	jogo = Game(2 , 1000)
	jogo.givePlayersCards()
	jogo.showCardsOnHand()
	jogo.Flop()
	jogo.showCardsOnTable()
	jogo.turn()
	jogo.showCardsOnTable()
	jogo.River()
	jogo.showCardsOnTable()

main()
	