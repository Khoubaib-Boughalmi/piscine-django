import sys
import random

with open("periodic_table.txt", "r") as f:
    lines = f.readlines()

def parse_line(line):
    res={}
    res["name"]=line.split("=")[0].strip()
    newline=line[len(res["name"])+3:-1]

    final_list=newline.split(",")
    for el in final_list:
        (key,value)=el.split(":")
        res[key.strip()]=value.strip()
    res["row"]=res["electron"].count(" ")
    return res

_List=[]
for line in lines:
    dataline=parse_line(line)
    _List.append(dataline)

def print_filled_atom(name, number, small, position, molar):
    # Generate random RGB values for the background color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    background_color = f"rgba({r}, {g}, {b}, 0.5)"

    atom = f"""
        <td style="border: 1px solid black; padding:10px; background-color: {background_color}">
            <h4>{name}</h4>
            <ul>
                <li>No {number}</li>
                <li>{small}</li>
                <li>{molar}</li>
                <li>{number} electron</li>
            </ul>
        </td>
    """
    return atom

def print_empty_atom():
    atom = f"""
        <td>
        </td>
    """
    return atom


def table_core():
    core_txt = ""
    pos = 0
    for row in range(7):
        core_txt += "<tr>"
        for col in range(18):
            if(_List[pos]["position"] == str(col)):
                core_txt += print_filled_atom(_List[pos]["name"],_List[pos]["number"], _List[pos]["small"], _List[pos]["position"], _List[pos]["molar"] )
                pos += 1
            else:
                core_txt += print_empty_atom()
        core_txt += "</tr>"
    return core_txt


def table_structure():
    #write into file

    structure = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <table style="border-collapse: collapse;">
                {table_core()}
            </table>
        </body>
        </html>
    """
    with open("periodic_table.html", "w") as f:
        f.write(structure)

    return structure

table_structure()