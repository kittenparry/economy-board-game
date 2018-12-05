
class property():
    def __init__(self, name, cost, colour, position, houses, hotel, rent):
        self.name = name
        self.cost = cost
        self.colour = colour
        self.position = position
        self.houses = houses
        self.hotel = hotel
        self.owner = None
        self.house_count = 0
        self.has_hotel = False
        self.rent = rent
class chance():
    def __init__(self, name, position):
        self.name = name
        self.position = position
class station():
    def __init__(self, name, cost, position):
        self.name = name
        self.cost = cost
        self.position = position
        self.owner = None
class util():
    def __init__(self, name, cost, position):
        self.name = name
        self.cost = cost
        self.position = position
        self.owner = None
class tax():
    def __init__(self, name, cost, position):
        self.name = name
        self.cost = cost
        self.position = position
class misc():
    def __init__(self, name, position):
        self.name = name
        self.position = position
props = []
chances = []
stations = []
utils = []
taxes = []
miscs = []
tiles = []
availables = []
def make_properties():
    #probably could do a for loop below?
    #a dictionary maybe?
    names = open(r'p\names.txt').read().split('\n')
    costs = list(map(int, open(r'p\costs.txt').read().split('\n')))
    colours = open(r'p\colours.txt').read().split('\n')
    positions = list(map(int, open(r'p\positions.txt').read().split('\n')))
    houses = open(r'p\houses.txt').read().split('\n') #houses[0].split(' ') for individual values
    hotels = list(map(int, open(r'p\hotels.txt').read().split('\n')))
    rents = list(map(int, open(r'p\rents.txt').read().split('\n')))
    for x in range(len(names)):
        props.append(property(names[x], costs[x], colours[x], positions[x], houses[x], hotels[x], rents[x]))
def make_chances():
    names = open(r'c\names.txt').read().split('\n')
    positions = list(map(int, open(r'c\positions.txt').read().split('\n')))
    for x in range(len(names)):
        chances.append(chance(names[x], positions[x]))
def make_stations():
    #all cost 200
    names = open(r's\names.txt').read().split('\n')
    costs = 200
    positions = list(map(int, open(r's\positions.txt').read().split('\n')))
    for x in range(len(names)):
        stations.append(station(names[x], costs, positions[x]))
def make_utils():
    #both cost 150
    names = ["Electric Company", "Water Works"]
    costs = 150
    positions = [12, 28]
    for x in range(len(names)):
        utils.append(util(names[x], costs, positions[x]))
def make_taxes():
    names = ["Income Tax", "Luxury Tax"]
    costs = [200, 100]
    positions = [4, 38]
    for x in range(len(names)):
        taxes.append(tax(names[x], costs, positions[x]))
def make_miscs():
    #Collect $200 salary as you pass
    names = ["GO", "In Jail/Just Visiting", "Free Parking", "Go to Jail"]
    positions = [0, 10, 20, 30]
    for x in range(len(names)):
        miscs.append(misc(names[x], positions[x]))
def make_tiles():
    #gameboard is 40 tiles (0-39)
    for x in range(40):
        for l in props, chances, stations, utils, taxes, miscs:
            for p in l: #l is a list, p is an object
                if p.position == x:
                    tiles.insert(40, p)
    for x in range(40):
        for l in props, stations, utils:
            for p in l:
                if p.position == x:
                    availables.insert(40, p)
