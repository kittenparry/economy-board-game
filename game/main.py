from game.make_properties import property_list
from game.players import player

property_list()
p1 = player("P1♞")

print(p1.position)
p1.move(39)
p1.roll_die()
print(p1.position)
print(p1.avatar)
