def readInto(name):
    stuff = open(name, "r", encoding="utf-8").read()
    data = [item.int() for item in stuff.strip().split('\n')]
    for thing in data:
        print(thing)