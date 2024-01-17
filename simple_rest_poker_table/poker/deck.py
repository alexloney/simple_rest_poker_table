import random

from simple_rest_poker_table.poker.card import Card
from simple_rest_poker_table.poker.enums.suit import Suit

class Deck:
    def __init__(self):
        self.stack = []
        self.discard = []
        self.dealt = []
    
    def create_standard_deck(self) -> None:
        self.stack = []
        self.discard = []
        self.dealt = []
        for suit in Suit:
            for rank in range(2, 15):
                self.stack.append(Card(rank, suit))
    
    def shuffle(self) -> None:
        while len(self.discard) > 0:
            self.stack.append(self.discard.pop())
        while len(self.dealt) > 0:
            self.stack.append(self.dealt.pop())
        random.shuffle(self.stack)
    
    def draw_card(self) -> Card:
        if len(self.stack) > 0:
            card = self.stack.pop()
            self.dealt.append(card)
            return card
        return None

    def __str__(self) -> str:
        result = '['
        first = True
        for card in self.stack:
            if first:
                first = False
            else:
                result += ', '
            result += str(card)
        result += ']'

        return result