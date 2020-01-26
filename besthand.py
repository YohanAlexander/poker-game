from cartas import Cards


class BestHand:
    def __init__(self, PT):
        self.__winningHand = 0
        self.__playerTable = PT
        self.__straight = list()
        self.__flush = list()
        self.__par = list()
        self.__trinca = list()
        self.__quadra = list()
        self.__fullHouse = list()
        self.__doisPares = list()
        self.__straightFlush = False
        self.checkPTQ()
        self.checkStraight()
        self.checkFlush()
        self.checkSpecialCases()

    def checkStraight(self):
        self.__straightCards = list()
        counter = 1
        n = 1
        for i in self.__playerTable:
            if(n < len(self.__playerTable)):
                if(i.getSimbol() == self.__playerTable[n].getSimbol() - 1):
                    if(i not in self.__straightCards):
                        self.__straightCards.append(i)
                    if(self.__playerTable[n] not in self.__straightCards):
                        self.__straightCards.append(self.__playerTable[n])
                    counter += 1
                    n += 1
                elif(i.getSimbol() == self.__playerTable[n].getSimbol()):
                    if(i not in self.__straightCards):
                        self.__straightCards.append(i)
                    if(self.__playerTable[n] not in self.__straightCards):
                        self.__straightCards.append(self.__playerTable[n])
                    n += 1
                else:
                    self.__straightCards = list()
                    n += 1
                    counter = 1
                if(counter >= 5):
                    self.__straight = self.__straightCards

    def checkFlush(self):
        self.__suitList = list()
        for i in self.__playerTable:
            self.__suitList.append(i.getSuit())
        if(self.__suitList.count("Copas") >= 5):
            for u in self.__playerTable:
                if(u.getSuit() == "Copas"):
                    self.__flush.append(u)
        elif(self.__suitList.count("Ouros") >= 5):
            for u in self.__playerTable:
                if(u.getSuit() == "Ouros"):
                    self.__flush.append(u)
        elif(self.__suitList.count("Espadas") >= 5):
            for u in self.__playerTable:
                if(u.getSuit() == "Espadas"):
                    self.__flush.append(u)
        elif(self.__suitList.count("Paus") >= 5):
            for u in self.__playerTable:
                if(u.getSuit() == "Paus"):
                    self.__flush.append(u)

    def checkPTQ(self):
        for i in self.__playerTable:
            count = 0
            index = 0
            self.__result = list()
            while(index < len(self.__playerTable)):
                if(i.getSimbol() == self.__playerTable[index].getSimbol()):
                    self.__result.append(self.__playerTable[index])
                    count += 1
                index += 1
            if(count == 4):
                if(self.__result[0] not in self.__par):
                    self.__quadra.append(self.__result[3])
                    self.__quadra.append(self.__result[2])
                    self.__quadra.append(self.__result[1])
                    self.__quadra.append(self.__result[0])
            elif(count == 3):
                if(self.__result[0] not in self.__trinca):
                    self.__trinca.append(self.__result[2])
                    self.__trinca.append(self.__result[1])
                    self.__trinca.append(self.__result[0])
            elif(count == 2):
                if(self.__result[0] not in self.__par):
                    self.__par.append(self.__result[1])
                    self.__par.append(self.__result[0])

    def checkSpecialCases(self):
        # FULLHOUSE:
        if(len(self.__par) > 0 and len(self.__trinca) > 0):
            self.__fullHouse = [self.__trinca[len(self.__trinca)-1], self.__trinca[len(self.__trinca)-2], self.__trinca[len(
                self.__trinca)-3], self.__par[len(self.__par)-2], self.__par[len(self.__par)-1]]

        # DOIS PARES:
        if(len(self.__par) > 2):
            self.__doisPares = [self.__par[len(self.__par)-1], self.__par[len(
                self.__par)-2], self.__par[len(self.__par)-3], self.__par[len(self.__par)-4]]

        # STRAIGHT FLUSH:
        if(len(self.__flush) > 0):
            counter = 1
            n = 1
            for i in self.__flush:
                if(n < len(self.__flush)):
                    if(i.getSimbol() == self.__flush[n].getSimbol() - 1):
                        counter += 1
                        n += 1
                    elif(i.getSimbol() == self.__playerTable[n].getSimbol()):
                        n += 1
                    else:
                        n += 1
                        counter = 1
                    if(counter >= 5):
                        self.__straightFlush = True

    def bestHandCondition(self):
        if(self.__straightFlush == True):
            return(9)
        elif(len(self.__quadra) > 0):
            return(8)
        elif(len(self.__fullHouse) > 0):
            return(7)
        elif(len(self.__flush) > 0):
            return(6)
        elif(len(self.__straight) > 0):
            return(5)
        elif(len(self.__trinca) > 0):
            return(4)
        elif(len(self.__doisPares) > 0):
            return(3)
        elif(len(self.__par) > 0):
            return(2)
        else:
            return(1)

    def bestHandConditionName(self):
        if(self.__straightFlush == True):
            return("Straight Flush!")
        elif(len(self.__quadra) > 0):
            return("Quadra!")
        elif(len(self.__fullHouse) > 0):
            return("Full House!")
        elif(len(self.__flush) > 0):
            return("Flush")
        elif(len(self.__straight) > 0):
            return("Straight!")
        elif(len(self.__trinca) > 0):
            return("Trinca.")
        elif(len(self.__doisPares) > 0):
            return("Dois pares.")
        elif(len(self.__par) > 0):
            return("Um par.")
        else:
            return("Carta alta.")

    def bestHand(self):
        if(self.__straightFlush == True):
            return([self.__flush[len(self.__flush)-5], self.__flush[len(self.__flush)-4], self.__flush[len(self.__flush)-3], self.__flush[len(self.__flush)-2], self.__flush[len(self.__flush)-1]])

        elif(len(self.__quadra) > 0):
            self.__winningHand = [self.__quadra[len(self.__quadra)-4], self.__quadra[len(
                self.__quadra)-3], self.__quadra[len(self.__quadra)-2], self.__quadra[len(self.__quadra)-1]]
            n = len(self.__playerTable) - 1
            while(n > 0):
                if(self.__playerTable[n] not in self.__winningHand):
                    self.__winningHand.append(self.__playerTable[n])
                    return(self.__winningHand)
                n -= 1

        elif(len(self.__fullHouse) > 0):
            return(self.__fullHouse)

        elif(len(self.__flush) > 0):
            return([self.__flush[len(self.__flush)-5], self.__flush[len(self.__flush)-4], self.__flush[len(self.__flush)-3], self.__flush[len(self.__flush)-2], self.__flush[len(self.__flush)-1]])

        elif(len(self.__straight) > 0):
            return([self.__straight[len(self.__straight)-5], self.__straight[len(self.__straight)-4], self.__straight[len(self.__straight)-3], self.__straight[len(self.__straight)-2], self.__straight[len(self.__straight)-1]])

        elif(len(self.__trinca) > 0):
            self.__winningHand = [self.__trinca[len(
                self.__trinca)-3], self.__trinca[len(self.__trinca)-2], self.__trinca[len(self.__trinca)-1]]
            n = len(self.__playerTable) - 1
            m = 0
            while(n > 0):
                if(self.__playerTable[n] not in self.__winningHand):
                    self.__winningHand.append(self.__playerTable[n])
                    m += 1
                if(m == 2):
                    return(self.__winningHand)
                n -= 1

        elif(len(self.__doisPares) > 0):
            self.__winningHand = [self.__doisPares[len(self.__doisPares)-4], self.__doisPares[len(
                self.__doisPares)-3], self.__doisPares[len(self.__doisPares)-2], self.__doisPares[len(self.__doisPares)-1]]
            n = len(self.__playerTable) - 1
            while(n > 0):
                if(self.__playerTable[n] not in self.__winningHand):
                    self.__winningHand.append(self.__playerTable[n])
                    return(self.__winningHand)
                n -= 1

        elif(len(self.__par) > 0):
            self.__winningHand = [
                self.__par[len(self.__par)-2], self.__par[len(self.__par)-1]]
            n = len(self.__playerTable) - 1
            m = 0
            while(n > 0):
                if(self.__playerTable[n] not in self.__winningHand):
                    self.__winningHand.append(self.__playerTable[n])
                    m += 1
                if(m == 3):
                    return(self.__winningHand)
                n -= 1

        else:
            self.__winningHand = [self.__playerTable[len(self.__playerTable)-5], self.__playerTable[len(self.__playerTable)-4], self.__playerTable[len(
                self.__playerTable)-3], self.__playerTable[len(self.__playerTable)-2], self.__playerTable[len(self.__playerTable)-1]]
            return(self.__winningHand)
