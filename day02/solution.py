from operator import mod

def part1(data):
    sumOfInvalid = 0
    for line in data.split(','):
        start, end = getStartAndEnd(line)
        for number in range(start, end + 1):
            if isInvalid(number):
                sumOfInvalid += number

    return sumOfInvalid

def getStartAndEnd(rangeStr):
    startStr, endStr = rangeStr.split('-')
    return int(startStr), int(endStr)

def isInvalid(number):
    strNum = str(number)
    length = len(strNum)
    if length % 2 != 0:
        return False
    
    half = length // 2
    return strNum[:half] == strNum[half:]

def part2(data):
    sumOfInvalid = 0
    for line in data.split(','):
        start, end = getStartAndEnd(line)
        for number in range(start, end + 1):
            if isInvalidPartII(number):
                sumOfInvalid += number

    return sumOfInvalid

def isInvalidPartII(number):
    strNum = str(number)
    length = len(strNum)
    if length == 1:
        return False
    
    maxSublen = length // 2
    for sublen in range(1, maxSublen + 1):
        if length % sublen != 0:
            continue

        sub = strNum[:sublen]
        if sub * (length // sublen) == strNum:
            return True

    return False


with open("day02/input.txt") as f:
    data = f.read().strip()

print('part1:', part1(data))
print('part2:', part2(data))