#!/bin/python

def getAndMakeAscii(char):
    ascii = ord(char)
    if(ascii < 91):
        return ascii - 64 + 26
    return ascii - 96


def controlgroup(group):
    for char in group[0]:
        if(char in group[1]):
            if(char in group[2]):
                return getAndMakeAscii(char)
    print("error")
    print(group)
    return 0


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getCode(lines):
    points = 0
    counter = 0
    group = ['', '', '']
    for line in lines:
        string = line.strip()
        group[counter] = string
        counter+=1
        if(counter > 2):
            points += controlgroup(group)
            counter = 0

    return points


def main():
    lines = getLines()
    points = getCode(lines)
    print(points)


main()
