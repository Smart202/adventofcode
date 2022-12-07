#!/bin/python

def getAndMakeAscii(char):
    ascii = ord(char)
    if(ascii < 91):
        return ascii - 64 + 26
    return ascii - 96


def controlLine(first, second):
    for char in second:
        if(char in first):
            return getAndMakeAscii(char)
    print("error")
    return 0


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getCode(lines):
    points = 0
    for line in lines:
        string = line.strip()
        firstHalf = string[:int(len(string) - (len(string) / 2))]
        secondHalf = string[int(len(string) / 2):]
        points += controlLine(firstHalf, secondHalf)

    return points


def main():
    lines = getLines()
    points = getCode(lines)
    print(points)


main()
