import re

def checkBeverageName(name):
    if len(name) > 15 or len(name) < 2:
        return False

    digits = re.search("\d", name)
    nonAlphabetical = re.search("\W", name)

    if digits is not None or nonAlphabetical is not None:
        return False

    return True

def checkSizes(sizes):
    sizesString = ''.join(sizes)
    notDigit = re.search("\D", sizesString)

    if notDigit is not None:
        return False
    
    parsedSizes = list(map(lambda x: int(x), sizes))

    if len(parsedSizes) < 1 or len(parsedSizes) > 5:
        return False

    repeated = set()
    sizesCopy = parsedSizes[:]
    sizesCopy.sort()

    if parsedSizes != sizesCopy:
        return False

    for size in parsedSizes:
        print(size)
        if size < 1 or size > 48:
            return False
        else:
            if size in repeated:
                return False
            repeated.add(size)

    return True

def checkData(data):
    if '' in data:
        return False

    if len(data) < 2 or len(data) > 6:
        return False
    
    return True

def addBeverage(name):
    print("Added beverage : ", name)

def addSizes(sizes):
    print("Added sizes: ", sizes)

def formatData(data):
    cleanedData = data.replace(" ", "")
    listedData = cleanedData.split(",")

    return listedData


def readData(data):
    formatedData = formatData(data)

    if not checkData(formatedData):
        return 

    beverageName = formatedData[0]
    
    if not checkBeverageName(beverageName):
        return 
    
    addBeverage(beverageName)
    
    sizes = formatedData[1:]

    if not checkSizes(sizes):
        return 
    
    addSizes(sizes)

    return True