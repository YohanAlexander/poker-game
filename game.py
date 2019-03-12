from nipePack import Deck
from player import Player

class Game:
	def __init__(self, nOPlayers, startingMonay = None):
		self.__players = list()
		
		self.__gameDeck = Deck()
		self.__gameDeck.initDeck()
		
		self.__gameTable = list()
		
		while(nOPlayers != 0):
			player = Player(startingMonay)
			self.__players.append(player)
			nOPlayers -= 1

	def givePlayersCards(self):
		j = 1
		while(j<=2):
			for i in self.__players:
				i.addToHand(self.__gameDeck.takeCard())
			j += 1
	
	def Flop(self):
		k = 1
		while(k<=3):
			self.__gameTable.append(self.__gameDeck.takeCard())
			k += 1
	
	def Turn(self):
		self.__gameTable.append(self.__gameDeck.takeCard())
	
	def River(self):
		self.__gameTable.append(self.__gameDeck.takeCard())
	
	def showFlop(self):
		print("Flop: " + self.__gameTable[0].showCard() + self.__gameTable[1].showCard() + self.__gameTable[2].showCard())
	
	def showTurn(self):
		print("Turn: " + self.__gameTable[3].showCard())
	
	def showRiver(self):
		print("River: " + self.__gameTable[4].showCard())
	
	def showCardsOnTable(self):
		print("Mesa: " + self.__gameTable[0].showCard() + self.__gameTable[1].showCard() + self.__gameTable[2].showCard() + self.__gameTable[3].showCard() + self.__gameTable[4].showCard())
	
	def showCardsOnHand(self):
		for i in self.__players:
			i.showHand()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
