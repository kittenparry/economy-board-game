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
            props.remove(property)
            #probably need to remove it from the bank's pool
            #need a better way, this also removes the ability to check the current tile
        else:
            print(strings("no_money"))

    def roll_die(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        print("%d and %d, a total of %d." % (self.die1, self.die2, (self.die1 + self.die2)))
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
        self.cur_prop = next((p for p in props if p.position == self.position), None)
        #if none check others here?
        print("%d is %s." % (self.position, self.cur_prop.name))
        print("%s has $%d, %s costs $%d." % (self.avatar, self.money, self.cur_prop.name, self.cur_prop.cost))
        #if can afford 110% of the cost
        if (self.money * 1.1) >= self.cur_prop.cost:
            print("%s decides to buy %s." % (self.avatar, self.cur_prop.name))
            self.buy(self.cur_prop, self.cur_prop.cost)
        else:
            print("%s decides to not buy %s. It's in auction now." % (self.avatar, self.cur_prop.name))

