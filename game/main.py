from game.properties import tiles, availables
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
    begin = game(4)
    for p in players:
        print(p.avatar, p.ai)
    print(availables[0].owner)
    players[1].buy(availables[1])
    players[0].move(3)
    print(availables[1].owner.avatar)
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
