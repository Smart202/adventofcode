#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getCode(lines):
    points = 0
    for line in lines:
        string = line.strip()
        pairs = string.split(',')
        point = checkPairs(pairs[0], pairs[1])
        points += point

    return points


def checkPairs(one, two):
    oneZero, oneTwo = one.split('-')
    twoZero, twoTwo = two.split('-')
    oneZero, oneTwo, twoZero, twoTwo = int(oneZero), int(oneTwo), int(twoZero), int(twoTwo)
    if(oneZero < twoZero):
        if(oneTwo >= twoTwo):
            return 1
    elif(twoZero < oneZero):
        if(twoTwo >= oneTwo):
            return 1
    elif(oneZero == twoZero):
        return 1
    return 0


def main():
    lines = getLines()
    points = getCode(lines)
    print(points)


main()
