#!/bin/python
import json


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines

def sortValues(left, right):
    print("comparing: ", left, " vs ", right)
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            print(left, "<", right, " - sorted")
            return -1
        if left > right:
            print(left, ">", right, " - not sorted")
            return 1
        return 0
    if isinstance(left, list):
        if isinstance(right, list):
            return isSorted(left, right)
        return isSorted(left, [right])
    return isSorted([left], right)


def isSorted(left,right):
    print("comparing: ", left, " vs ", right)
    leftLen = len(left)
    rightLen = len(right)
    if rightLen and not leftLen:
        return -1
    if leftLen and not rightLen:
        return 1
    for index in range(0,leftLen):
        if index > rightLen-1:
            return 1
        sortValue = sortValues(left[index], right[index])
        if sortValue == 1:
            print("",left[index]," vs ", right[index])
            return 1
        if sortValue == -1:
            print("",left[index]," vs ", right[index])
            return -1
    if rightLen > leftLen:
        return -1
    return 0

def makeInput(lines):
    counter = 0
    left = False
    right = False
    pairCounter = 0
    finalValue = 0
    for line in lines:
        line = line.strip()
        if line == "":
            counter = 0
            continue
        if counter == 0:
            left = json.loads(line)
        else:
            pairCounter+=1
            right = json.loads(line)
            print(" ")
            print("---------","Checking pair #", pairCounter,"-----------")
            print(left)
            print("vs")
            print(right)
            checkSort = isSorted(left, right)
            if checkSort != 1:
                finalValue += pairCounter
                print("sorted") 
            else:
                print("not sorted")
            print(" ")
            #if pairCounter >70:
                #input("Press Enter to continue...")

        counter+=1

    return finalValue





def main():
    lines = getLines()
    input = makeInput(lines)
    print(input)


main()
