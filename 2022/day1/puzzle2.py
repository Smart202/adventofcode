#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getMaxValue(lines):
    maxValues = [0, 0, 0]
    currentValue = 0
    for line in lines:

        if(line == '\n'):
            if(currentValue > maxValues[2]):
                maxValues[0] = maxValues[1]
                maxValues[1] = maxValues[2]
                maxValues[2] = currentValue
            elif(currentValue > maxValues[1]):
                 maxValues[0] = maxValues[1]
                 maxValues[1] = currentValue
            elif(currentValue > maxValues[0]):
                maxValues[0] = currentValue
            currentValue = 0
        else:
            size = len(line)
            string = line[:size-1]
            value = int(string)
            currentValue+=value

    return maxValues[0] + maxValues[1] + maxValues[2]


def main():
    lines = getLines()
    maxValue = getMaxValue(lines)
    print(maxValue)


main()
