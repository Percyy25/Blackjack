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
        self.cards = []

    def built_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11
        }

        for suit in suits:
            for rank, value in ranks.items():
                card = (rank, value, suit)
                self.cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Player:

    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for card in deck:
            deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        for card in self.hand:
            card.display_card()

    def hit(self, deck):
        self.hand.append(deck.deal_card())

    def get_hand(self):
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print(self.hand_value)

    def update_hand(self, deck):
        if self.hand_value < 21:
            if input("Would you like to hit?").capitalize() == "Yes":
                self.hit(deck)
            else:
                self.playing_hand = False
        else:
            self.playing_hand = False
class the_dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for card in deck:
            deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        show_cards = input("Press enter to reveal the dealer's cards.")
        if show_cards == "":
            for card in self.hand:
                time.sleep(1)
                print(card)

    def get_hand_value(self):
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value
            if card.suit == "A":
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10

    def hit(self, deck):
        if self.hand_value <= 17:
            self.hand.append(deck.deal_card())
            self.get_hand_value()



