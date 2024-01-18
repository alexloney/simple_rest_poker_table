from simple_rest_poker_table.poker.dealer.dealer import Dealer
from simple_rest_poker_table.poker.table import Table
from simple_rest_poker_table.poker.player import Player
from simple_rest_poker_table.poker.deck import Deck

import logging

class TexasHoldEmDealer(Dealer):
    def __init__(self):
        self.deck = Deck()
        self.pot = 0
        self.small_blind = 1
        self.big_blind = 2
        self.board = []
    
    def start_game(self):

        # Basic validation on number of players for a game
        player_count = 0
        for player in self.table.players:
            if not player.sitting_out:
                player_count += 1

        if player_count < 2:
            raise Exception("Too few players to play")
        if player_count > 23:
            raise Exception("Too many players to play")
        
        logging.info("Game starting")
        self.deck.create_standard_deck()
        self.deck.shuffle()
        logging.info("Deck: " + str(self.deck))

        logging.info("Collecting blinds from players")
        pos = 0
        small_blind_taken = False
        big_blind_taken = False
        for player in self.table.players:
            if small_blind_taken and big_blind_taken:
                break
            if not player.sitting_out:
                if not small_blind_taken:
                    cash = player.request_small_blind(self.small_blind)
                    if cash is not None:
                        logging.info("Received small blind from Player " + str(pos+1))
                        self.pot += cash
                        small_blind_taken = True
                    else:
                        logging.info("Player " + str(pos+1) + " refused small blind, player is now sitting out")
                        player.sitting_out = True
                elif not big_blind_taken:
                    cash = player.request_big_blind(self.big_blind)
                    if cash is not None:
                        logging.info("Received big blind from Player " + str(pos+1))
                        self.pot += cash
                        big_blind_taken = True
                    else:
                        logging.info("Player " + str(pos+1) + " refused big blind, player is now sitting out")
                        player.sitting_out = True
                pos += 1
        
        logging.info("Game pot is now: " + str(self.pot))

        # Deal two cards to each player
        for i in range(0, 2):
            for player in self.table.players:
                if not player.sitting_out:
                    player.give_card(self.deck.draw_card())
        
        pos = 0
        for player in self.table.players:
            if not player.sitting_out:
                logging.info("Player " + str(pos+1) + ": " + str(player))
                pos += 1
        
        # TODO: Next up, we need to loop through the players and request if they
        #       want to check, bet, call, or fold. This will repeat until everyone
        #       has checked.
        
        logging.info("Dealing flop")
        for i in range(0, 3):
            self.board.append(self.deck.draw_card())
        logging.info("Board: " + ', '.join([str(x) for x in self.board ]))

        # TODO: Next betting round

        logging.info("Dealing Turn")
        self.board.append(self.deck.draw_card())
        logging.info("Board: " + ', '.join([str(x) for x in self.board ]))

        # TODO: Next betting round

        logging.info("Dealing river")
        self.board.append(self.deck.draw_card())
        logging.info("Board: " + ', '.join([str(x) for x in self.board ]))

        # TODO: Final betting round

        # TODO: Tally winner

        # TODO: Assign winnings
