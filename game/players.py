from game.strings import strings
from game.properties import *
from game.cards import *
import random

players = []
class player():
    def __init__(self, avatar, ai):
        self.money =  1500
        self.properties = []
        self.position = 0
        self.avatar = avatar
        self.double_die = 0
        self.ai = ai
        self.bid = 0
        self.get_out_of_jail = 0
        self.in_jail = False
        self.is_bankrupt = False

    def buy(self, property, bid = None):
        if bid == None:
            cost = property.cost
        else:
            cost = bid
            #auction if not purchased
        if self.money >= cost:
            self.money -= cost
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
                self.position = tiles[10].position #jail
                self.double_die = 0
            else:
                self.move(self.dies)
                if self.die1 == self.die2:
                    #needs to purchase/pay rent etc before rerolling
                    #we are doing the purchases with .move() so it should be alright
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
                            self.auction(self.cur_tile)
                            break
                        else:
                            print("Enter y or n only.")
        elif self.cur_tile in decks:
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

    def auction(self, property):
        print("%s decides not to buy %s. An auction is now in session.\nHighest bidder gets the property." % (self.avatar, property.name))
        self.auction_bid = 1
        #self.ai_bids = 0 #do an increase with each turn?
        #while True:
        for p in players[1:]: #ai bidding
            self.auction_bid = random.randint(self.auction_bid, (p.money/5)) #1/4th is low?
            p.bid = self.auction_bid
            #this is flawed because as long as the last robot has money, it will get the property
            #instead do randomize bids without giving a low limit of auction_bid to solve?
        print("Bids so far are:")
        for p in players[1:]:
            print("%s\t$%d" % (p.avatar, p.bid))
        print("Enter an amount between $%d-$%d. Or type \"skip\"." % (self.auction_bid, self.money))
        while True:
            try:
                str = input()
                try:
                    self.bid = int(str)
                except ValueError:
                    pass
                if str == "skip":
                    #selling to the highest bidder here
                    for p in players:
                        if self.auction_bid == p.bid:
                            p.buy(property, p.bid)
                            print("%s is the highest bidder with $%d." % (p.avatar, p.bid))
                    break
                elif self.bid > self.auction_bid and self.bid <= self.money:
                    #buying self here
                    print("%s is the highest bidder with $%d." % (self.avatar, self.bid))
                    self.buy(property, self.bid)
                    break
                else:
                    print("Please enter only numbers between $%d-$%d. Or type \"skip\"." % (self.auction_bid, self.money))
            except ValueError:
                print("Please enter only numbers between $%d-$%d. Or type \"skip\"." % (self.auction_bid, self.money))
    def choose_mortgage(self, fee):
        print("%s currently has $%d and need a total of $%d." % (self.avatar, self.money, fee))
        #maybe put above to move?
        if len(self.properties) > 0:
            print("Choose one of the following to mortgage by typing its ID.")
            print("ID\tValue\tColour\tName")
            temp_list = []
            x = 0
            for p in self.properties:
                if not p.is_mortgaged:
                    x += 1
                    print("%d\t$%d\t%s\t%s" % (x, (p.cost/2), p.colour, p.name))
                    temp_list.append(p)
            while True:
                try:
                    s = int(input())
                    self.mortgage(temp_list[s-1], fee)
                    break
                except (ValueError, IndexError):
                    print("Enter a number between 1-%d." % (len(temp_list)))
        else:
            self.bankruptcy()
    def mortgage(self, property, fee):
        #need to sell houses? before mortgaging
        property.is_mortgaged = True
        self.money += property.cost/2
        if self.money >= fee:
            print("%s mortgaged %s for $%d and paid their debt of $%d." % (self.avatar, property.name, property.cost/2, fee))
            self.money -= fee
        else:
            print("%s mortgaged %s for $%d and paid some of their debt." % (self.avatar, property.name, property.cost/2))
            leftover = fee - self.money
            self.money = 0
            self.choose_mortgage(leftover)
    def bankruptcy(self):
        print("%s didn't have the property or money to pay their debt and is bankrupt." % self.avatar)
        self.is_bankrupt = True
        #add an if not is_bankrupt switch to every action or remove them from player pool?
    def ai_turn(self):
        print("%s is rolling..." % self.avatar)
        self.temp_pos = self.position
        self.roll_die()
        print("%s is moving from %d to %d." % (self.avatar, self.temp_pos, self.position))
        self.cur_tile = next((p for p in props if p.position == self.position), None)
        #if none check others here?
        #props, decks, stations, utils, taxes, miscs
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
    def chance(self, c_or_cc):
        if c_or_cc: #chance
            cur_card = chances[0]
            chances.append(chances.pop(0)) #puts the card to the end of the list
            print("Chance!")
            print(cur_card.desc)
            self.id_chance(cur_card.id)
        else: #community chest
            cur_card = chests[0]
            chests.append(chests.pop(0))
            print("Community Chest!")
            print(cur_card.desc)
            self.id_chest(cur_card.id)
    def id_chance(self, id):
        if id == 0:
            self.cc_advance_to_go()
        elif id == 1:
            self.c_advance_to_x(24)
        elif id == 2:
            self.c_advance_to_x(11)
        elif id == 3:
            self.c_advance_to_util()
        elif id == 4 or id == 5:
            self.c_advance_to_station()
        elif id == 6:
            self.cc_collect_money(50)
        elif id == 7:
            self.cc_get_out_of_jail()
        elif id == 8:
            self.c_go_back_3_spaces()
        elif id == 9:
            self.cc_go_to_jail()
        elif id == 10:
            self.cc_pay_for_houses_hotels(25, 100)
        elif id == 11:
            self.cc_pay_money(15)
        elif id == 12:
            self.c_advance_to_x(5)
        elif id == 13:
            self.c_advance_to_x(39)
        elif id == 14:
            self.c_pay_players(50)
        elif id == 15:
            self.cc_collect_money(150)
        elif id == 16:
            self.cc_collect_money(100)
    def id_chest(self, id):
        if id == 0:
            self.cc_advance_to_go()
        elif id == 1:
            self.cc_collect_money(200)
        elif id == 2 or id == 11 or id == 12:
            self.cc_pay_money(50)
        elif id == 3:
            self.cc_collect_money(50)
        elif id == 4:
            self.cc_get_out_of_jail()
        elif id == 5:
            self.cc_go_to_jail()
        elif id == 6:
            self.cc_collect_from_players(50)
        elif id == 7 or id == 10 or id == 16:
            self.cc_collect_money(100)
        elif id == 8:
            self.cc_collect_money(20)
        elif id == 9:
            self.cc_collect_from_players(10)
        elif id == 13:
            self.cc_collect_money(25)
        elif id == 14:
            self.cc_pay_for_houses_hotels(40, 115)
        elif id == 15:
            self.cc_collect_money(10)
    ##community chests
    def cc_advance_to_go(self):
        self.move(0)
    def cc_collect_money(self, money):
        self.money += money
    def cc_pay_money(self, money):
        if self.money >= money:
            self.money -= money
        else:
            pass
            #mortgage etc. here
    def cc_get_out_of_jail(self):
        self.get_out_of_jail += 1
    def cc_go_to_jail(self):
        self.position = 10
        self.in_jail = True
    def cc_collect_from_players(self, money):
        temp_list = players.copy()
        temp_list.remove(self)
        for p in temp_list:
            if p.money >= money:
                self.money += money
                p.money -= money
            else:
                pass
                #mortgage etc. here
    def cc_pay_for_houses_hotels(self, house_cost, hotel_cost):
        house_count = 0
        hotel_count = 0
        fee = 0
        for p in props:
            if p.owner == self:
                house_count += p.house_count
                if p.has_hotel:
                    hotel_count += 1
        fee += (house_count * house_cost) + (hotel_count * hotel_cost)
        print("%s has a total of %d house(s) and %d hotel(s)." % (self.avatar, house_count, hotel_count))
        print("Total fee is %d." % fee)
        if self.money >= fee:
            self.money -= fee
        else:
            #mortgage etc. here
            pass
    ##chances
    def c_advance_to_x(self, x):
        if self.position > x: #If you pass Go, collect $200.
            self.money += 200
        self.move(x) #24 Trafalgar, 11 Pall, 5 Kings Cross, 39 Mayfair
    def c_advance_to_util(self):
        #Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown.
        if self.position > 12 and self.position < 28:
            self.move(28)
        else:
            self.move(12) #TODO: add special cases for 10x throws
        #check the rules for what happens if they are on the tile
        #same goes for the below one
    def c_advance_to_station(self):
        #Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.
        #2 of these ^
        if self.position > 35 and self.position < 5:
            self.move(5)
        elif self.position > 5 and self.position < 15:
            self.move(15)
        elif self.position > 15 and self.position < 25:
            self.move(25)
        else:
            self.move(35) #TODO: add special cases for 10x throws
    def c_go_back_3_spaces(self):
        self.move((self.position - 3) % 40)
    def c_pay_players(self, money):
        temp_list = players.copy()
        temp_list.remove(self)
        fee = money * len(temp_list)
        if self.money >= fee:
            for p in temp_list:
                p.money += money
            self.money -= fee
        else:
            #mortgage etc. here
            pass
