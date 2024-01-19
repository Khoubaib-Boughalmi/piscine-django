def readFromFile ():
    try:
        with open("numbers.txt", "r") as f: # with for auto close file
            x = f.read()
            for i in x.split(","):
                print(i.strip())

    except FileNotFoundError:
        print("File not found")

if __name__ == '__main__':
    readFromFile()