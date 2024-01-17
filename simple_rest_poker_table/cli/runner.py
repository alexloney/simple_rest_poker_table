import sys

from simple_rest_poker_table.poker.table import Table
from simple_rest_poker_table.poker.room import Room
from simple_rest_poker_table.poker.deck import Deck
from simple_rest_poker_table.poker.player import Player
from simple_rest_poker_table.poker.dealer.texas_hold_em_dealer import TexasHoldEmDealer

def cli():
    # TODO: CLI argument parsing?
    print("Here!")

    dealer = TexasHoldEmDealer()
    table = Table(dealer)
    player1 = Player()
    table.add_player(player1)
    player2 = Player()
    table.add_player(player2)
    room = Room()
    room.add_table(table)

    

    deck = Deck()
    deck.create_standard_deck()
    print(deck)
    deck.shuffle()
    print(deck)
    card = deck.draw_card()
    print(card)
    print(deck)
    deck.shuffle()
    print(deck)
    pass