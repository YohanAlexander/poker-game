class Player:
	def __init__(self, monay = 500):
		self.__hand = list()
		self.__monay = monay
	
	def showHand(self):
		print("Your hand: " + self.__hand[0].showCard() + " and " + self.__hand[1].showCard())
	
	def getMonay(self):
		return self.__monay
	
	def addToHand(self, Card):
		self.__append(card)