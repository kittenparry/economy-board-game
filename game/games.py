from game.players import player, players
from game.properties import *
from game.cards import *

class game():
    def __init__(self, player_count):
        self.player_count = player_count #this may be useless
        self.make_players(self.player_count)
        self.make_makes()
    def make_players(self, player_count):
        players.append(player("P1", False))
        for x in range(1, player_count):
            players.append(player("P%d" % (x+1), True))

    def make_makes(self):
        make_properties()
        make_decks()
        make_stations()
        make_utils()
        make_taxes()
        make_miscs()
        make_tiles()
        make_availables()
        make_cards()
