from game.players import player
from game.properties import make_properties

players = []
class game():
    def __init__(self, player_count):
        self.player_count = player_count #this may be useless
        self.make_players(self.player_count)
        make_properties()
    def make_players(self, player_count):
        for x in range(player_count):
            players.append(player("P%d" % (x+1)))
