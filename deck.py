from collections import deque
from random import shuffle

from .card import Card

class Deck:

    def __init__(self):
        card_list = self._create_deck()
        shuffled_cards = shuffle(card_list)
        self._cards = deque(shuffled_cards)

    def _create_deck(self):
        cards = []
        for suit in ["clubs", "spades", "diamonds", "hearts"]:
            for face in list(range(2, 11)):
                card = Card(suit, face, face)
                cards.append(card)
            cards.append(Card(suit, "A", 1))
            for face in ["J", "Q", "K"]:
                cards.append(Card(suit, face, 10))

    def next_card(self):
        return self._cards.popleft()

    def add_to_deck(self, card):
        self._cards.append()
