import re

def readInto(name):
    data = []
    stuff = open(name, "r", encoding="utf-8")
    reading = stuff.read()
    x = bool(re.search(",", reading))
    if (x):
        y = re.split("\n", reading)
        part = [item.partition(', ') for item in y]
        part.pop(len(part) - 1)
        Dict = {}
        for thing in part:
            Dict[int(thing[0])] = int(thing[2], 16)
        data = Dict
    else:
        data = [int(item) for item in reading.strip().split('\n')]
        for thing in data:
            print(thing)
    stuff.close()
    return data
    