from simple_rest_poker_table.poker.card import Card

class Player:
    def __init__(self):
        self.hand = []
        self.stack = 10
        self.sitting_out = False
    
    def give_card(self, card: Card):
        self.hand.append(card)
    
    def give_money(self, money: int):
        self.stack += money

    def request_small_blind(self, value):
        if self.stack >= value:
            self.stack -= value
            return value
        return None

    def request_big_blind(self, value):
        if self.stack >= value:
            self.stack -= value
            return value
        return None

    def remove_cards(self):
        self.hand = []

    def __str__(self):
        response = '['

        first = True
        for card in self.hand:
            if first:
                first = False
            else:
                response += ', '
            response += str(card)

        response += ', [stack: ' + str(self.stack) + ']'

        response += ']'
        return response