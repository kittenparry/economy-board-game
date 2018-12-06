
class card():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
chests = []
chances = []
def make_cards():
    cc_names = open(r'ca\community_chests.txt').read().split('\n')
    c_names = open(r'ca\chances.txt').read().split('\n')
    for x in range(len(cc_names)):
        chests.append(card("chest", cc_names[x]))
        chances.append(card("chance", c_names[x]))
#i suppose i also need to put their functions in player class
