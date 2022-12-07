#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getMaxValue(lines):
    maxValue = 0
    currentValue = 0
    for line in lines:
        
        if(line == '\n'):
            if(maxValue < currentValue):
                maxValue = currentValue
            currentValue = 0
        else:
            size = len(line)
            string = line[:size-1]
            value = int(string)
            currentValue+=value

    return maxValue


def main():
    lines = getLines()
    maxValue = getMaxValue(lines)
    print(maxValue)


main()
