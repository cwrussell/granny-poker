from collections import deque
from random import shuffle

from card import Card

class Deck:

    def __init__(self, values={}, waste=False):
        self._values = values
        if not waste:
            card_list = self._create_deck()
            shuffle(card_list)
        else:
            card_list = []
        self._cards = deque(card_list)
        
    DEFAULT_VALUES = {
        "A": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
        10: 10, "J": 10, "Q": 10, "K": 10
    }
    
    def _get_default_values(self):
        faces = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
        def_values = {face: i + 1 for i, face in enumerate(faces)}
        return def_values
        
    def _get_value(self, face):
        if face in self._values: return self._values[face]
        else: return self.DEFAULT_VALUES[face]

    def _create_deck(self):
        cards = []
        for suit in ["Clubs", "Spades", "Diamonds", "Hearts"]:
            for face in list(range(2, 11)):
                card = Card(suit, face, self._get_value(face))
                cards.append(card)
            cards.append(Card(suit, "A", self._get_value("A")))
            for face in ["J", "Q", "K"]:
                cards.append(Card(suit, face, self._get_value(face)))
        return cards

    def next_card(self):
        return self._cards.popleft()

    def to_right(self, card):
        self._cards.append(card)
        
    def to_left(self, card):
        self._cards.appendleft(card)
        
    def top(self):
        return str(self._cards[0])
        
    def deal(self, n_hands, n_cards):
        hands = [[] for i in range(n_hands)]
        for i in range(n_cards):
            for j in range(n_hands):
                hands[j].append(self.next_card())
        return hands

