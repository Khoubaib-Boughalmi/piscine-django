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

my_str = "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"

my_str_arr = my_str.split(",")

for i in range(len(my_str_arr)):
    my_str_arr[i] = my_str_arr[i].strip()
