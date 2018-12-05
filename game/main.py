from game.properties import tiles, props
from game.games import game, players
from game.strings import strings

def switch(val):
    s = {
        "s": states,
    }
    f = s.get(val)
    return f()

def states():
    print("#-Players-#-Pos-#-Money-#")
    for p in players:
        print("|{0:^9}|{1:5}|{2:7}|".format(p.avatar, p.position, p.money))
    print("#---------#-----#-------#")

def start():
    game(4)
    print(tiles)
    for x in tiles:
        print(x.name)
    #states()
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
