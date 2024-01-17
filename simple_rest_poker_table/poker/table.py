from simple_rest_poker_table.poker.player import Player
from simple_rest_poker_table.poker.dealer.dealer import Dealer

class Table:
    def __init__(self, dealer: Dealer):
        self.players = []
        self.dealer = dealer
    
    def add_player(self, player: Player):
        self.players.append(player)