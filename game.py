from deck import Deck
from player import Player
from table import Table
import os
import random
clear = lambda: os.system('cls')

class Game:
	def __init__(self):
		clear()
		self.__players = list()
		self.__playersOnRound = list()
		self.__gameDeck = Deck()
		self.__gameTable = Table()
		
	def addPlayers(self, nOPlayers, startingMonay):
		contador = 0
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
	
	def setDeck(self):
		self.__gameDeck.initDeck()
	
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
			if(len(self.__gameTable.getTable()) >= 5):
				print(i.getName() + ", sua mesa é: " + str(i.showPlayerTable()) + "\nVocê compete com: " + str(i.getBestHandConditionName()) + "\n" + "Sua mão em jogo é:" + str(i.showBestHand()) + "\n")
			else:
				print(i.getName() + ", sua mão é: " + i.showHand())
	
	def getNOPlayers(self):
		return len(self.__players)
		
	def getWinner(self):
		winner = self.checkWhoWon(self.__players)
		winners = list()
		if(len(winners) == 1):
			return winners[0].getName()
		else:
			for i in winner:
				winners.append(i.getName())
			return (winners)
				
	
	def showWinner(self):
		if(len(self.checkWhoWon(self.__players)) == 1):
			print("O vencedor é: " + self.getWinner()[0] + "!")
		else:
			if(len(self.checkWhoWon(self.__players)) == 2):
				print("Os vencedores são: " + self.getWinner()[0] + ", " + self.getWinner()[1] + "!\nO valor será dividido.")
			elif(len(self.checkWhoWon(self.__players)) == 3):
				print("Os vencedores são: " + self.getWinner()[0] + ", " + self.getWinner()[1] + ", " + self.getWinner()[2] + "!\nO valor será dividido.")
	
	def resetPlayersOnRound(self):
		self.__playersOnRound = list()
	
	def newGame(self):
		clear()
		self.setDeck()
		for i in self.__players:
			i.newTurn()
		self.resetPlayersOnRound()
		for i in self.__players:
			self.__playersOnRound.append(i.getName())
	
	def checkWhoWon(self, playerList):
		highestPointPlayers = list()
		for i in playerList:
			points = i.getBestHandCondition()
			if(len(highestPointPlayers) == 0):
				highestPointPlayers.append(i)
			elif(points > highestPointPlayers[0].getBestHandCondition()):
				highestPointPlayers = [i]
			elif(points == highestPointPlayers[0].getBestHandCondition()):
				highestPointPlayers.append(i)
		
		while(len(highestPointPlayers) > 1):
			handOne = highestPointPlayers[0].getBestHand()
			handTwo = highestPointPlayers[1].getBestHand()
			handIndex = 0
			isEqual = 0
			while(handIndex <= 4):
				if(handOne[handIndex].getSimbol() > handTwo[handIndex].getSimbol()):
					highestPointPlayers.pop(1)
					break
				elif(handOne[handIndex].getSimbol() < handTwo[handIndex].getSimbol()):
					highestPointPlayers.pop(0)
					break
				elif(handOne[handIndex].getSimbol() == handTwo[handIndex].getSimbol()):
					isEqual += 1
					handIndex += 1
			if(isEqual == 5):
				break
				
		return(highestPointPlayers)
	
	def waitForBets(self, playerIndex):
		while(True):
			startingIndex = playerIndex
			if(playerIndex == self.getNOPlayers()):
				playerIndex = 0
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	