class Hand():
    'A players or dealers hand'
    def __init__(self) -> None:
        self.hand = []
        self.blackJack = False

    def addCard(self, card):
        # self.hand.append(Deck.pickCard)
        self.hand.append(card)

    def clear(self):
        self.hand.clear()

    def getHandAmount(self):
        'number of cards'
        self.handValue = 0#total of hand?
        for card in self.hand:
            if(card[0] in ['Jack', 'Queen', 'King']):
                self.handValue += 10
            
            elif card[0] == 'Ace':
                if self.handValue <= 10:
                    self.handValue += 11
                else:
                    self.handValue += 1
            
            else:
                self.handValue += card[0]
        
        
        return self.handValue

    def setHandValue(self, value):
        self.handValue += value

    def getHandValue(self):
        return self.handValue

    def checkBlackJack(self):
        'return true if hand value == 21'
    
    def checkBust(self):
        'return true if hand is over 21'

    def __str__(self):
        hand = ""
        for card in self.hand:
            hand += f"{card[0]} of {card[1]}'s\n"
        return hand
