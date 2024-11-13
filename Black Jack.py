import random
import time

class Cards:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print(f"{self.rank} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards: []

    def built_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Splades"]
        ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
        "K": 10, "A": 11
        }

        for suit in suits:
            for rank, value in rank.items():
                card = (rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None