import random

class card():
    def __init__(self, name, desc, id):
        self.name = name
        self.desc = desc
        self.id = id
chests = []
chances = []
def make_cards():
    cc_names = open(r'card\community_chests.txt').read().split('\n')
    c_names = open(r'card\chances.txt').read().split('\n')
    for x in range(len(cc_names)):
        chests.append(card("chest", cc_names[x], x))
        chances.append(card("chance", c_names[x], x))
def shuffle_cards():
    random.shuffle(chests)
    random.shuffle(chances)
#i suppose i also need to put their functions in player class
#use the function switch from main.py for functions?
#need to shuffle cards before the game starts (should be in games.py)
