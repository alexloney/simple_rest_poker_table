from simple_rest_poker_table.poker.enums.suit import Suit

class Card:
    def __init__(self, rank: int, suit: Suit):
        if rank < 2 or rank > 14:
            raise Exception('Invalid card rank: ' + str(self.rank))
        
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        result = '['
        if self.rank == 14:
            result += 'A'
        elif self.rank == 13:
            result += 'K'
        elif self.rank == 12:
            result += 'Q'
        elif self.rank == 11:
            result += 'J'
        elif self.rank == 10:
            result += 'T'
        else:
            result += str(self.rank)
        
        if self.suit == Suit.SPADE:
            result += 's'
        elif self.suit == Suit.CLUB:
            result += 'c'
        elif self.suit == Suit.DIAMOND:
            result += 'd'
        elif self.suit == Suit.HEART:
            result += 'h'

        result += ']'

        return result