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

capital_value = capital_cities[states[sys.argv[1]]]
if capital_value:
    print(capital_value)
else:
    print("Unknown state")