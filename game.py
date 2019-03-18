from deck import Deck
from player import Player
from table import Table
import os
clear = lambda: os.system('cls')

class Game:
	def __init__(self, nOPlayers, startingMonay = None):
		clear()
		
		contador = 0
		self.__players = list()
		
		self.__gameDeck = Deck()
		self.__gameDeck.initDeck()
		
		self.__gameTable = Table()
		
		while(nOPlayers != 0):
			contador += 1
			name = str(input("Player " + str(contador) + " name: "))
			gplayer = Player(name, startingMonay)
			self.__players.append(gplayer)
			nOPlayers -= 1
			clear()

	def givePlayersCards(self):
		j = 1
		while(j<=2):
			for i in self.__players:
				card = self.__gameDeck.takeCard()
				i.addToHand(card)
				i.appendToPlayerTable(card)
			j += 1
	
	def Flop(self):
		k = 0
		while(k<=2):
			self.__gameDeck.cutCard()
			card = self.__gameDeck.takeCard()
			self.__gameTable.putOnTable(card)
			for i in self.__players:
				i.appendToPlayerTable(card)
			k += 1
	
	def Turn(self):
		self.__gameDeck.cutCard()
		card = self.__gameDeck.takeCard()
		self.__gameTable.putOnTable(card)
		for i in self.__players:
				i.appendToPlayerTable(card)
	
	def River(self):
		self.__gameDeck.cutCard()
		card = self.__gameDeck.takeCard()
		self.__gameTable.putOnTable(card)
		for i in self.__players:
				i.appendToPlayerTable(card)
	
	def showFlop(self):
		self.__gameTable.printFlop()
	
	def showTurn(self):
		self.__gameTable.printTurn()
	
	def showRiver(self):
		self.__gameTable.printRiver()
	
	def showCardsOnTable(self):
		self.__gameTable.printAllCardsOnTable()
	
	def showCardsOnHand(self):
		for i in self.__players:
			i.showHand()

	def showPlayerGame(self):
		for i in self.__players:
			print(i.getName() + ", sua mesa é: " + i.showPlayerTable() + "\nVocê compete com: " + i.getBestHandCondition() + "\n" + "Sua mão em jogo é:" + i.showBestHand() + "\n")
		
	
	def getNOPlayers(self):
		return len(self.__players)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
