from game.strings import strings
from game.properties import *
import random

class player():
    def __init__(self, avatar, ai):
        self.money =  1500
        self.properties = []
        self.position = 0
        self.avatar = avatar
        self.double_die = 0
        self.ai = ai

    def buy(self, property):
        #auction if not purchased
        if self.money >= property.cost:
            self.money -= property.cost
            self.properties.append(property) #this looks useless after adding owners
            property.owner = self
            #probably need to remove it from the bank's pool
            #need a better way, this also removes the ability to check the current tile
        else:
            print(strings("no_money"))

    def roll_die(self, s_util = None):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        #double test
        #self.die1 = 2
        #self.die2 = 2
        print("%d and %d, a total of %d." % (self.die1, self.die2, (self.die1 + self.die2)))
        if s_util == None:
            self.dies = (self.position + (self.die1 + self.die2)) % 40
            #check for doubles, etc
            if self.double_die >= 2:
                print("%s rolled 3 doubles back to back and will go to jail." % self.avatar)
                self.position = tiles[9].position #jail
                self.double_die = 0
            else:
                self.move(self.dies)
                if self.die1 == self.die2:
                    #needs to purchase/pay rent etc before rerolling
                    print("%s rolled a double and will roll again." % self.avatar)
                    self.double_die += 1
                    #shouldn't roll by itself again
                    #but how to manage ai?
                    if self.ai:
                        #self.roll_die()
                        #not really this ^
                        #but something else
                        pass
                if self.die1 != self.die2:
                    self.double_die = 0
        else:
            return (self.die1 + self.die2)

    def move(self, position):
        self.position = position
        self.cur_tile = tiles[self.position]
        #checks for special positions here
        #stations and utils also can be auctioned
        if self.cur_tile in availables:
            print("it's a prop")
            if self.ai:
                #ai stuff
                pass
            else:
                #it's owned by another player
                if self.cur_tile.owner != None and self.cur_tile.owner != self:
                    print("already owned")
                    self.pay_rent(self.cur_tile)

                else:
                    print("%d: %s, costs $%d. Purchase? (y/n)" % (self.position, self.cur_tile.name, self.cur_tile.cost))
                    while True:
                        i = input().lower()
                        if i == "y":
                            self.buy(self.cur_tile)
                            break
                        elif i == "n":
                            print("::Auction here")
                            break
                        else:
                            print("Enter y or n only.")
        elif self.cur_tile in chances:
            print("it's a chance")
        elif self.cur_tile in taxes:
            print("it's taxes")
        elif self.cur_tile in miscs:
            print("it's miscs")


    def pay_rent(self, property):
        if property in props:
            houses = list(map(int, property.houses.split(" ")))
            if property.house_count >= 1:
                rent = houses[property.house_count-1]
                print("%s has %d houses. Rent is $%d." % (property.name, property.house_count, rent))
            elif property.has_hotel:
                rent = property.hotel
                print("%s has a hotel. Rent is $%d." % (property.name, rent))
            else:
                rent = property.rent
                print("Rent of %s is $%d." % (property.name, rent))
        elif property in stations:
            station_count = 0
            for f in stations:
                if f.owner == property.owner:
                    station_count += 1
            if station_count == 4:
                rent = 200
            elif station_count == 3:
                rent = 100
            elif station_count == 2:
                rent = 50
            else:
                rent = 25
            print("%s owns %d station(s). Rent is $%d." % (property.owner.avatar, station_count, rent))
        else: #elif property in utils:
            #4xdice if 1 owned, 10xdice if 2.
            util_count = 0
            for f in utils:
                if f.owner == property.owner:
                    util_count += 1
            if util_count == 2:
                print("%s owns both of the utilities. Roll die and pay 10 times." % property.owner.avatar)
                rent = self.roll_die(True) * 10
            else:
                print("%s owns one of the utilities. Roll die and pay 4 times." % property.owner.avatar)
                rent = self.roll_die(True) * 4
        if self.money >= rent:
            self.money -= rent
            property.owner.money += rent
            print("%s has paid %s a total of $%d." % (self.avatar, property.owner.avatar, rent))
        else:
            print("Not enough money to pay the rent.")
            #mortgage etc. here
    def ai_turn(self):
        print("%s is rolling..." % self.avatar)
        self.temp_pos = self.position
        self.roll_die()
        print("%s is moving from %d to %d." % (self.avatar, self.temp_pos, self.position))
        self.cur_tile = next((p for p in props if p.position == self.position), None)
        #if none check others here?
        #props, chances, stations, utils, taxes, miscs
        if self.cur_tile is None:
            self.cur_tile = next((p for p in props if p.position == self.position), None)
        print("%d is %s." % (self.position, self.cur_tile.name))
        print("%s has $%d, %s costs $%d." % (self.avatar, self.money, self.cur_tile.name, self.cur_tile.cost))
        #if can afford 110% of the cost
        if (self.money * 1.1) >= self.cur_tile.cost:
            print("%s decides to buy %s." % (self.avatar, self.cur_tile.name))
            self.buy(self.cur_tile)
        else:
            print("%s decides to not buy %s. It's in auction now." % (self.avatar, self.cur_tile.name))

