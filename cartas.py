class Cards:
	def __init__(self, nipe, simbol):
		self.__nipe = nipe
		self.__simbol = simbol
	
	def getNipe(self):
		return self.__nipe
		
	def getSimbol(self):
		return self.__simbol
	
	def showCard(self):
		print(self.__nipe + ":" + self.__simbol + " ")