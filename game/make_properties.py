from game.strings import strings
from game.properties import property

def make_properties():
    pass
    #objects here

def property_list():
    #probably could do a for loop below?
    names = open(r'p\names.txt').read().split('\n')
    costs = open(r'p\costs.txt').read().split('\n')
    colours = open(r'p\colours.txt').read().split('\n')
    positions = open(r'p\positions.txt').read().split('\n')
    houses = open(r'p\houses.txt').read().split('\n') #houses[0].split(' ') for individual values
    hotels = open(r'p\hotels.txt').read().split('\n')
    props = []
    for x in range(len(names)):
        props.append(property(names[x], costs[x], colours[x], positions[x], houses[x], hotels[x]))
        #print(props[x].name)
