import sys

if len(sys.argv) != 2:
    sys.exit(0)

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

state_name = sys.argv[1]
print (capital_cities[states[state_name]])