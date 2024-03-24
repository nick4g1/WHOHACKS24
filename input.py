import re

def readInto(name):
    data = []
    stuff = open(name, "r", encoding="utf-8")
    reading = stuff.read()
    x = bool(re.search(",", reading))
    if (x):
        y = re.split("\n", reading)
        part = [item.partition(', ') for item in y]
        #print(part)
        part.pop(len(part) - 1)
        for thing in part:
            obj = Pair(thing[0], int(thing[2], 16))
            data.append(obj)
    stuff.close()
    print(data)
    return data

class Pair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"<Pair with Key:{self.key} Value:{self.value}>"
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    