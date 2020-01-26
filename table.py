class Table:
    def __init__(self):
        self.__table = list()
        self.__pot = 0

    def putOnTable(self, card):
        self.__table.append(card)

    def printFlop(self):
        print("Flop: " + self.__table[0].showCard() +
              self.__table[1].showCard() + self.__table[2].showCard())

    def printTurn(self):
        print("Turn: " + self.__table[3].showCard())

    def printRiver(self):
        print("River: " + self.__table[4].showCard() + "\n")

    def printAllCardsOnTable(self):
        print("Mesa: " + self.__table[0].showCard() + self.__table[1].showCard(
        ) + self.__table[2].showCard() + self.__table[3].showCard() + self.__table[4].showCard() + "\n")

    def getTable(self):
        return self.__table

    def addToPot(self, value):
        self.__pot += value

    def getPot(self):
        return self.__pot
