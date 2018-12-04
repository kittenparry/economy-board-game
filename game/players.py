from game.strings import strings
import random

class player():
    def __init__(self, avatar):
        self.money =  1500
        self.properties = []
        self.position = 0
        self.avatar = avatar

    def buy(self, property, cost):
        #auction if not purchased
        if self.money >= cost:
            self.money -= cost
            self.properties.append(property)
            #probably need to remove it from the bank's pool
        else:
            print(strings("no_money"))

    def roll_die(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        print("%d + %d" % (self.die1, self.die2))
        self.dies = (self.position + (self.die1 + self.die2)) % 40
        #check for doubles, etc
        self.move(self.dies)
    def move(self, position):
        self.position = position
