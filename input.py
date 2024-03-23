def readInto(name):
    stuff = open(name, "r", encoding="utf-8")
    reading = stuff.read()
    stuff.close()
    data = [int(item) for item in reading.strip().split('\n')]
    for thing in data:
        print(thing)
    return data
    