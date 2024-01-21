import sys
import os
import re

def check_number_args() :
    if (len(sys.argv) != 2):
        print("Wrong number of args")
        exit(1)

def check_file_extension (templateFile):
    if (len(templateFile.split(".")) != 2):
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

setting_obj = {}

def parse_settings_file(settingsList):
    global setting_obj
    for item in settingsList:
        key = item.split("=")[0]
        value = item.split("=")[1]
        setting_obj[str(key).strip()] = value.strip()

def inject_values_into_template(templateList, settingsList):
    pattern = r'\{([^}]+)\}'
    populated_template = ""
    
    for line in templateList:
        res = re.search(pattern, line)
        if(res):
            populated_template += line[:res.start()]
            while(res) :
                populated_template += setting_obj.get(res.group(1), "").replace("\"", "")
                line = line[res.end():]
                res = re.search(pattern, line)
                if(res):
                    populated_template += line[:res.start()]
                else:
                    populated_template += line[:]
        else:
            populated_template += line
    return populated_template

def generate_html(populated_template):
    final_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {populated_template}
    </body>
    </html>
    """
    return final_html

if __name__ == '__main__':
    check_number_args()
    check_file_extension(sys.argv[1])
    templateList = check_template_file(sys.argv[1])
    settingsList = check_and_get_settings_file()
    parse_settings_file(settingsList)
    populated_template = inject_values_into_template(templateList, settingsList)
    final_html = generate_html(populated_template)
    with open("views.html", "w") as f:
        f.write(final_html)