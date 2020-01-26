from cartas import Cards
from besthand import BestHand


class Player:
    def __init__(self, playerName, monay):
        self.__playerName = playerName
        self.__monay = monay
        self.__monayOnPot = 0
        self.__hand = list()
        self.__playerTable = list()
        self.__winningHandCondition = 0
        self.__winningHand = 0
        self.__isBig = False
        self.__isSmall = False

    def getName(self):
        return str(self.__playerName)

    def getMonay(self):
        return self.__monay

    def addMonay(self, value):
        self.__monay += value

    def getMonayOnPot(self):
        return self.__monayOnPot

    def bet(self, value):
        if(value <= self.__monay):
            self.__monay -= value
            self.__monayOnPot += value

    def getIsBig(self):
        return(self.__isBig)

    def getIsSmall(self):
        return(self.__isSmall)

    def switchBig(self):
        if(self.__isBig == False):
            self.__isBig = True
        else:
            self.__isBig = False

    def switchSmall(self):
        if(self.__isSmall == False):
            self.__isSmall = True
        else:
            self.__isSmall = False

    def showHand(self):
        if(len(self.__hand) == 2):
            return(self.__hand[0].showCard() + " e " + self.__hand[1].showCard() + "\n")
        else:
            return("Nada em mãos.")

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

    def addToHand(self, card):
        self.__hand.append(card)

    def appendToPlayerTable(self, card):
        self.__playerTable.append(card)

    def newTurn(self):
        self.__playerTable = list()
        self.__hand = list()
        self.__winningHandCondition = 0
        self.__winningHand = 0
        self.__monayOnPot = 0

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

    def getBestHandConditionName(self):
        self.organizeHand()
        self.__winningHandCondition = BestHand(self.__playerTable)
        return self.__winningHandCondition.bestHandConditionName()

    def getBestHand(self):
        self.organizeHand()
        self.__winningHand = BestHand(self.__playerTable)
        return self.__winningHand.bestHand()

    def showBestHand(self):
        bestCards = self.getBestHand()
        return(bestCards[0].showCard() + bestCards[1].showCard() + bestCards[2].showCard() + bestCards[3].showCard() + bestCards[4].showCard())
