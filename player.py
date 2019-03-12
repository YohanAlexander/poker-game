from cartas import Cards
class Player(Cards):
	def __init__(self, monay = 500):
		self.__hand = list()
		self.__monay = monay
	
	def showHand(self):
		print("Sua mão: " + self.__hand[0].showCard() + " e " + self.__hand[1].showCard())
	
	def getMonay(self):
		return self.__monay
	
	def addToHand(self, card):
		self.__hand.append(card)
