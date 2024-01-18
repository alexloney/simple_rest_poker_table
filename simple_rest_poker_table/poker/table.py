from simple_rest_poker_table.poker.dealer.dealer import Dealer
from simple_rest_poker_table.poker.player import Player

class Table:
    def __init__(self, dealer: Dealer):
        self.players = []
        self.dealer = dealer
        self.dealer.assign_table(self)

    def add_player(self, player: Player):
        self.players.append(player)