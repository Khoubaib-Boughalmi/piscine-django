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

my_str = "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"

def get_key_from_value(d, needle):
    for key, value in d.items():
        if needle == value:
            return key
    return None

def split_input(input):
    my_str_arr = my_str.split(",")

    for i in range(len(my_str_arr)):
        my_str_arr[i] = my_str_arr[i].strip().lower().capitalize()

    return my_str_arr

def get_state(state):
    for key, value in states.items():
        if key.lower() == state.lower():
            return key
    return None

def get_capital(capital):
    for key, value in capital_cities.items():
        if value.lower() == capital.lower():
            return value
    return None


def get_key_from_value(d, needle):
    for key, value in d.items():
        if needle == value:
            return key
    return None

def get_state_from_capital(capital):
    capital_key = get_key_from_value(capital_cities, capital);
    state = get_key_from_value(states, capital_key)
    return state

def get_capital_from_state(state):
    if state == "New jersey":
        return "Trenton"
    return capital_cities[states[state]]

def display_output():
    list_input = split_input(sys.argv[1])
    for item in list_input:
        if item == "":
            continue
        if get_state(item):
            print(get_capital_from_state(item) + " is the capital of " + get_state(item))
        elif get_capital(item):
            print(get_capital(item) + " is the capital of " + get_state_from_capital(item))
        else:
            print(item + " is neither capital city nor a state")

display_output()