from deck import Deck
from hand import Hand


class Dealer():
    def __init__(self):
        self.hand = Hand()
        self.deck = Deck()
        self.name = "Dealer"
        self.isStanding = True #haven't busted yet.
        self.isVictor = False #Won hand

    def dealPlayers(self, Player):
        'deal card to other players'
        card = self.deck.pickCard()
        Player.hand.addCard(card)
        print(f"Dealing {card[0]} of {card[1]}'s to {Player.name}")

    def dealSelf(self):
        card = self.deck.pickCard()
        self.hand.addCard(card)


    def checkWinnings(self, player):
        #player won black jack (21)
        if(player.getBlackJack()):
            player.blackJackWinnings()
        #player had over 21 cards or has a lesser hand than dealer
        elif player.getHandAmount() > 21 or (self.getHandAmount() > player.getHandAmount() and self.getHandAmount() <= 21):
            player.bust()
        
        elif(player.getHandAmount() == self.getHandAmount()):
            player.push()

        #player won the round
        else:
            player.wonRound()

        
        


    def dealerShuffle(self):
        'shuffle cards'
        self.deck.shuffle()

    def clearHand(self):
        self.hand.clear()

    def clearCards(self):
        'return all the cards from the players and reshuffle'
        self.deck.generateDeck()

    def generateDeck(self):
        self.deck.generateDeck()

    def getHandAmount(self):
        return self.hand.getHandAmount()

    def getHand(self, revealSecond):
        'get the cards in players hand'
        #only print the first card. Other card is kept secret
        if not revealSecond:
            print(f"{self.name}")
            print(f"{self.hand.hand[0][0]} of {self.hand.hand[0][1]}'s")
            return
        print()
        print(f"{self.name}:")
        print(self.hand)
        print()
