from game.strings import strings
from game.properties import props
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
        print("%d and %d" % (self.die1, self.die2))
        self.dies = (self.position + (self.die1 + self.die2)) % 40
        #check for doubles, etc
        self.move(self.dies)
    def move(self, position):
        self.position = position

    def ai_turn(self):
        print("%s is rolling..." % self.avatar)
        self.temp_pos = self.position
        self.roll_die()
        print("%s is moving from %d to %d." % (self.avatar, self.temp_pos, self.position))
        print("%d is %s." % (self.position, next((p.name for p in props if int(p.position) == self.position), None)))
