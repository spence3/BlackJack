from player import Player
from dealer import Dealer
from deck import Deck

    
class Blackjack():
    def __init__(self):
        self.dealer = Dealer()
        self.playerLyst = []
        self.numPlayers = 0
        self.MAX_PLAYERS = 5

    def addPlayer(self):
        self.numPlayers += 1
        name = input(f"Player {self.numPlayers} what is your name?: ")
        bank = float(input("How much are you bringing to the table?: "))
        player = Player(name, bank)
        self.playerLyst.append(player)

    def setUp(self):
        numofPlayers = int(input("How many players are playing?: "))
        while self.numPlayers > self.MAX_PLAYERS:
            numofPlayers = int(input("How many players are playing?: "))

        for i in range(numofPlayers):
            self.addPlayer()

    def round(self):
        for player in self.playerLyst:
            player.getHand()
            hitOrStay = input(f"{player.name}, type h for hit or s for stay?: ")
            
            while(hitOrStay != 'h' and hitOrStay != 's'):
                hitOrStay = input(f"{player.name}, type h for hit or any other key for stay: ")

            while(hitOrStay == "h" and player.getHandAmount() < 21):
                self.dealer.dealPlayers(player)
                player.getHand()
                hitOrStay = input(f"{player.name}, type h for hit or any other key for stay: ")

    def StartGame(self):
        while self.numPlayers > 0:
            self.dealer.generateDeck()
            self.dealer.dealerShuffle()
            
            # Add players if open seats
            while self.numPlayers < self.MAX_PLAYERS:
                revealSecond = False #wait to revel the dealers second card
                addPlayers = input("Are there any players that would like to join? "
                               "Press 'y' for yes and 'n' for no: ")
                if addPlayers == 'y':
                    self.addPlayer()
                    break  
                else:
                    break

            #place bets
            for player in self.playerLyst:
                bet = int(input(f"{player.name} you have ${player.bank} to bet. how much would you like too bet?: "))
                while player.bank < bet:
                    bet = int(input(f"{player.name} you have ${player.bank} to bet. how much would you like too bet?: "))
                player.setBet(bet)

            #first card dealt to players
            for player in self.playerLyst:
                self.dealer.dealPlayers(player)

            #dealer deals card to self(dealer)
            self.dealer.dealSelf()

            #deal players second card
            for player in self.playerLyst:
                self.dealer.dealPlayers(player)
                print(f"{player.getName()}:\n you have {player.getBank()} in your bank and you have bet ${player.getBet()}")
                player.getHand()
                player.getHandAmount()


            self.dealer.dealSelf()
            self.dealer.getHand(revealSecond)
            revealSecond = True #now the dealer can reveal the second card



            self.round()
            #dealer deals second hadn
            self.dealer.getHand(revealSecond)
            #go until dealers hand reaches 17 - 21
            while(self.dealer.getHandAmount() < 17):
                for player in self.playerLyst:
                    player.getHand()
                    hitOrStay = input(f"{player.name}, type h for hit or s for stay?: ")
                    
                    while(hitOrStay != 'h' and hitOrStay != 's'):
                        hitOrStay = input(f"{player.name}, type h for hit or any other key for stay: ")

                    while(hitOrStay == "h"):
                        self.dealer.dealPlayers(player)
                        player.getHand()
                        hitOrStay = input(f"{player.name}, type h for hit or any other key for stay: ")

                self.dealer.dealSelf()
                self.dealer.getHand(revealSecond)
            
            for player in self.playerLyst:
                self.dealer.checkWinnings(player)

            
            for player in self.playerLyst:
                player.clearHand() #reset their cards to null
                player.setBlackJack()
                print(player)


            self.dealer.clearHand()
            self.dealer.clearCards()#reset the deck



def main():
    blackJackGame = Blackjack()
    blackJackGame.setUp()
    blackJackGame.StartGame()


    

if __name__ == "__main__":
    main()