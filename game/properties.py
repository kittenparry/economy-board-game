
class property():
    def __init__(self, name, cost, colour, position, houses, hotel):
        self.name = name
        self.cost = cost
        self.colour = colour
        self.position = position
        self.houses = houses
        self.hotel = hotel

props = []
def make_properties():
    #probably could do a for loop below?
    #a dictionary maybe?
    names = open(r'p\names.txt').read().split('\n')
    costs = open(r'p\costs.txt').read().split('\n')
    colours = open(r'p\colours.txt').read().split('\n')
    positions = open(r'p\positions.txt').read().split('\n')
    houses = open(r'p\houses.txt').read().split('\n') #houses[0].split(' ') for individual values
    hotels = open(r'p\hotels.txt').read().split('\n')
    for x in range(len(names)):
        props.append(property(names[x], costs[x], colours[x], positions[x], houses[x], hotels[x]))
