from cartas import Cards
from besthand import BestHand

class Player(Cards):
	def __init__(self, playerName, monay = 500):
		self.__playerName = playerName
		self.__monay = monay
		self.__hand = list()
		self.__playerTable = list()
		self.__winningHandCondition = 0
		self.__winningHand = 0
	
	def showHand(self):
		if(len(self.__hand) == 2):
			print(str(self.__playerName) + " : " + self.__hand[0].showCard() + " e " + self.__hand[1].showCard() + "\n")
		else:
			print("Nada em mãos.")
	
	def showPlayerTable(self):
		self.organizeHand()
		if(len(self.__playerTable) == 7):
			return(self.__playerTable[0].showCard() + self.__playerTable[1].showCard() + self.__playerTable[2].showCard() + self.__playerTable[3].showCard() + self.__playerTable[4].showCard() + self.__playerTable[5].showCard() + self.__playerTable[6].showCard())
		elif(len(self.__playerTable) == 6):
			return(self.__playerTable[0].showCard() + self.__playerTable[1].showCard() + self.__playerTable[2].showCard() + self.__playerTable[3].showCard() + self.__playerTable[4].showCard() + self.__playerTable[5].showCard())
		elif(len(self.__playerTable) == 5):
			return(self.__playerTable[0].showCard() + self.__playerTable[1].showCard() + self.__playerTable[2].showCard() + self.__playerTable[3].showCard() + self.__playerTable[4].showCard())
		elif(len(self.__playerTable) == 2):
			self.showHand()
	
	def getMonay(self):
		return self.__monay
	
	def addToHand(self, card):
		self.__hand.append(card)
	
	def getName(self):
		return str(self.__playerName)
	
	def appendToPlayerTable(self, card):
		self.__playerTable.append(card)
	
	def newTurn(self):
		self.__playerTable = list()
		self.__hand = list()
		self.__winningHandCondition = 0
		self.__winningHand = 0
	
	def organizeHand(self):
		while(True):
			m = 0
			modded = 0
			while(m < len(self.__playerTable) - 1):
				if(self.__playerTable[m].getSimbol() > self.__playerTable[m+1].getSimbol()):
					modded = 1
					temp = self.__playerTable[m]
					self.__playerTable[m] = self.__playerTable[m + 1]
					self.__playerTable[m + 1] = temp
				m += 1
			if(modded == 0):
				break
	
	def getBestHandCondition(self):
		self.organizeHand()
		self.__winningHandCondition = BestHand(self.__playerTable)
		return self.__winningHandCondition.bestHandCondition()
	
	def getBestHand(self):
		self.organizeHand()
		self.__winningHand = BestHand(self.__playerTable)
		return self.__winningHand.bestHand()
	
	def showBestHand(self):
		bestCards = self.getBestHand()
		return(bestCards[0].showCard() + bestCards[1].showCard() + bestCards[2].showCard() + bestCards[3].showCard() + bestCards[4].showCard())
		
		
		
		
		

		
		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
