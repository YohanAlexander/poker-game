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

	def givePlayersCards():
		j = 1
		while(j<=2):
			for j in self.__players:
				j.addToHand(self.__gameDeck.takeCard())
			j = j+1
	
	def Flop(self):
		k = 1
		while(k<=3):
			self.__gameTable.append(self.__gameDeck.takeCard())
			k = k+1
	
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
		self.showFlop()
		self.showTurn()
		self.showRiver()
	
	def showCardsOnHand(self):
		for i in self.__players(self):
			i.showHand()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	