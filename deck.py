from cartas import Cards
import random


class Deck:
    def __init__(self):
        self.__deck = list()

    def initDeck(self):
        i = 2
        while (i <= 13):
            carta = Cards("Ouros", i)
            self.__deck.append(carta)
            i = i+1
        i = 2
        while (i <= 13):
            carta = Cards("Copas", i)
            self.__deck.append(carta)
            i = i+1
        i = 2
        while (i <= 13):
            carta = Cards("Paus", i)
            self.__deck.append(carta)
            i = i+1
        i = 2
        while (i <= 13):
            carta = Cards("Espadas", i)
            self.__deck.append(carta)
            i = i+1

    def takeCard(self):
        card = random.choice(self.__deck)
        self.__deck.remove(card)
        return card

    def cutCard(self):
        card = random.choice(self.__deck)
        self.__deck.remove(card)
