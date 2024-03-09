from hand import Hand

class Player():

    def __init__(self, name, bank):
        self.hand = Hand()
        self.name = name
        self.origBank = bank
        self.bank = bank #how much the player starts with
        self.bet = 0
        self.isStanding = True #True for now
        self.blackJack = False #first hand is an ace and a 10
        self.isVictor = False #hasn't won yet
        self.handValue = 0

    def hit(self):
        'get another card'
    
    def setBlackJack(self):
        self.blackJack = False
    
    def getBlackJack(self):
        if(self.getHandAmount() == 21):
            self.blackJack = True
        return self.blackJack
    
    def blackJackWinnings(self):
        winning = self.bet * 1.5
        self.bank += self.bet + winning
        print(f"You Won ${winning} You now have ${self.bank}")
        self.clearBet()

    def wonRound(self):
        self.bank += self.bet * 2
        print(f"You Won ${self.bet} You now have ${self.bank}")
        self.clearBet()

    def bust(self):
        print(f"You lost ${self.bet} You now have ${self.bank}")
        self.clearBet()

    def push(self):
        'play nor dealer wins'
        self.bank += self.bet
        print(f"You tied the dealer You still have ${self.bank}")
        self.clearBet()

    def clearBet(self):
        self.bet = 0

    def doubleDown(self):
        'double down'

    def betAmount(self):
        'amount being bet'
        return self.bet

    def winnings(self):
        'how much the player has when they quit'

    def insurance(self):
        pass

    def setIsVictor(self):
        'Won round'
        self.isVictor = True

    def getIsStanding(self):
        'does not take any additional cards'

    def getName(self):
        'return players name'
        return self.name

    def getBank(self):
        'return players total'
        return self.bank
    
    def getBet(self):
        return self.bet
    
    def setBet(self, bet):
        self.bet = bet
        self.bank -= bet
    
    def getHand(self):
        'get the cards in players hand'
        print(f"{self.name}'s Hand:")
        print(self.hand)

    def clearHand(self):
        self.hand.clear()

    def getHandAmount(self):
        return self.hand.getHandAmount()


    def __str__(self):
        if self.origBank < self.bank:
            return f"{self.name} You gotta step it up. Who's going to pay for your rent? You have less than what you did before with ${self.bank}"
        
        elif self.origBank == self.bank:
            return f"{self.name} You gotta start making some moves my boy"

        else:
            return f"{self.name} You're a dawg, keep killing it with this moneeeeyyy"