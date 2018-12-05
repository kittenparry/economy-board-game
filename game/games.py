from game.players import player
from game.properties import *

players = []
class game():
    def __init__(self, player_count):
        self.player_count = player_count #this may be useless
        self.make_players(self.player_count)
        self.make_makes()
        self.bank = bank()
    def make_players(self, player_count):
        for x in range(player_count):
            players.append(player("P%d" % (x+1)))
    def make_makes(self):
        make_properties()
        make_chances()
        make_stations()
        make_utils()
        make_taxes()
        make_miscs()
        make_tiles()
class bank():
    def __init__(self):
        self.properties = []
        for x in range(40):
            for l in props, stations, utils:
                for p in l: #l is a list, p is an object
                    if p.position == x:
                        self.properties.insert(40, p)
