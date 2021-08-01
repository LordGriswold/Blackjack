class Card:
    def __init__(self, value):
        self.__value = value
        self.__suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.__ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                        "King"]

    def getRank(self):
        return self.__ranks[self.__value % 13]

    def getSuit(self):
        return self.__suits[self.__value // 13]

    def getCardValue(self):
        return self.__value % 13 + 1

    def getDeckValue(self):
        return self.__value

    def getNickName(self):
        nick_name = ""
        if 1 < self.getCardValue() < 11:
            nick_name += str(self.getCardValue())
        else:
            nick_name += self.getRank()[0]

        nick_name += self.getSuit()[0]

        return nick_name

    # Dunder to return a string representation to print() and format()
    def __str__(self):
        return self.getRank() + " of " + self.getSuit()

    # Dunder to return a string representation to other usages
    def __repr__(self):
        return self.__str__()
