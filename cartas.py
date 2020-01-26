class Cards:
    def __init__(self, suit, simbol):
        self.__suit = suit
        self.__simbol = simbol

    def getSuit(self):
        return self.__suit

    def getSimbol(self):
        return self.__simbol

    def showCard(self):
        return str(self.__suit + ":" + str(self.__simbol) + " ")
