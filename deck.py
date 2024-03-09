import itertools
import random

class Deck():
    def __init__(self):
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = list(itertools.product(self.ranks, self.suits))
        self.used_cards = []#cards that have been used already... might remove


    def shuffle(self):
        return random.shuffle(self.deck)
    
    def pickCard(self):
        card = random.choice(self.deck)
        self.used_cards.append(card)
        self.deck.remove(card)
        return card

    def generateDeck(self):
        self.deck.extend(self.used_cards)
        self.used_cards.clear()
    

