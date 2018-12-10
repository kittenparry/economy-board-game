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
    players[0].move(37)
    states()
    players[0].roll_die()
    states()
    #players[0].ai_turn()
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
