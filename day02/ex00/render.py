import sys
import os
import re

def check_number_args() :
    if (len(sys.argv) != 2):
        print("Wrong number of args")
        exit(1)

def check_file_extension (templateFile):
    if (len(templateFile.split(".") != 2)):
        print("Error: Wrong file extension format")
        exit(1)
    ext = templateFile.split(".")[1]
    if (ext != "template"):
        print("Error: Wrong file extension")
        exit(1)

def check_and_get_settings_file() :
    settings = []
    try:
        with open("settings.py", "r") as f:
            settings = f.readlines()
    except FileNotFoundError:
        print("Error: no settings.py file")
        exit(1)
    return settings

def check_template_file(templateFile) :
    template = []
    try:
        with open(templateFile, "r") as f:
            template = f.readlines()
    except FileNotFoundError:
        print(f"Error: no {templateFile} file")
        exit(1)
    return template


if __name__ == '__main__':
    check_number_args()
    check_file_extension(sys.argv[1])
    print(check_template_file(sys.argv[1]))
