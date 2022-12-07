#!/bin/python

def getValue(letter):
    if(letter == "A" or letter == "X"):
        return 1
    elif(letter == "B" or letter == "Y"):
        return 2
    elif(letter == "C" or letter == "Z"):
        return 3


def winRound(you):
    if(you == "A"):
        return "Y"
    elif(you == "B"):
        return "Z"
    else:
        return "X"
def loseRound(you):
    if(you == "A"):
        return "Z"
    elif(you == "B"):
        return "X"
    else:
        return "Y"

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def calculatePoints(you, me):
    if(me == "X"):
        return 0 + getValue(loseRound(you))
    elif(me == "Y"):
        return 3 + getValue(you)
    else:
        return 6 + getValue(winRound(you))


def getCode(lines):
    points = 0
    for line in lines:
        string = line.split('\n')
        x = string[0].split(' ')
        aux = calculatePoints(x[0], x[1])
        #print("points: " + str(aux) + " - " + x[0] + "("+str(getValue(x[0]))+") vs " + x[1] +"("+str(getValue(x[1]))+")")
        points += aux
    return points


def main():
    lines = getLines()
    points = getCode(lines)
    print(points)


main()
