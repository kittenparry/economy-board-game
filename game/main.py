from game.properties import *
from game.games import game, players
from game.strings import strings
from game.cards import *

def states():
    print("#-Players-#-Pos-#-Money-#")
    for p in players:
        print("|{0:^9}|{1:5}|{2:7}|".format(p.avatar, p.position, int(p.money)))
    print("#---------#-----#-------#")

def start():
    begin = game(4)
    states()
    #players[0].chance(True)
    availables[0].owner = players[0]
    props[1].owner = players[0]
    players[0].properties.append(availables[0])
    players[0].properties.append(props[1])
    players[0].money = 0
    players[0].choose_mortgage(35)
    states()
    #players[0].ai_turn()
    #switch("s") #states() is shorter...
    #while True:
        #turns, playing, stuff here
        #probably need an ai
        #foreach players?
        #cmd = input()

if __name__ == '__main__':
    '''
    #commented for quicker testing
    print("Number of players?")
    try:
        p = int(input())
        game(p)
        start()
    except ValueError:
        print(strings("err_pc")) #between 2-4.
    '''
    #game(4)
    start()
