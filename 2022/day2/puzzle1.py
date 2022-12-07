#!/bin/python

def getValue(letter):
    if(letter == "A" or letter == "X"):
        return 1
    elif(letter == "B" or letter == "Y"):
        return 2
    elif(letter == "C" or letter == "Z"):
        return 3


def winRound(you, me):
    if(you == "A"):
        if(me == "Y"):
            return True
    elif(you == "B"):
        if(me == "Z"):
            return True
    else:
        if(me == "X"):
            return True
    return False


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def calculatePoints(you, me):
    if(getValue(you) == getValue(me)):
        return 3 + getValue(me)
    elif(winRound(you, me)):
        return 6 + getValue(me)
    else:
        return getValue(me)


def getCode(lines):
    points = 0
    for line in lines:
        string = line.split('\n')
        x = string[0].split(' ')
        aux = calculatePoints(x[0], x[1])
        print("points: " + str(aux) + " - " + x[0] + "("+str(getValue(x[0]))+") vs " + x[1] +"("+str(getValue(x[1]))+")")
        points += aux
    return points


def main():
    lines = getLines()
    points = getCode(lines)
    print(points)


main()
