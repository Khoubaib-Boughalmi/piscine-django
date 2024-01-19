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

def get_key_from_value(d, needle):
    for key, value in d.items():
        if needle == value:
            return key
    return None

capital = get_key_from_value(capital_cities, sys.argv[1]);
state = get_key_from_value(states, capital)

if state:
    print(state)
else:
    print("Unknown state")