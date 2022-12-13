#!/bin/python
import json


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if isSorted(arr[j], arr[j + 1]) == 1:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


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


def isSorted(left, right):
    print("comparing: ", left, " vs ", right)
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]
    leftLen = len(left)
    rightLen = len(right)
    if rightLen and not leftLen:
        return -1
    if leftLen and not rightLen:
        return 1
    for index in range(0, leftLen):
        if index > rightLen-1:
            return 1
        sortValue = sortValues(left[index], right[index])
        if sortValue == 1:
            print("", left[index], " vs ", right[index])
            return 1
        if sortValue == -1:
            print("", left[index], " vs ", right[index])
            return -1
    if rightLen > leftLen:
        return -1
    return 0


def makeInput(lines):
    div1 = [[2]]
    div2 = [[6]]
    l = [div1, div2]
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        l.append(json.loads(line))

    bubbleSort(l)

    dividerLocationOne = l.index(div1) + 1
    dividerLocationTwo = l.index(div2) + 1
    print(len(l))
    return dividerLocationOne * dividerLocationTwo


def main():
    lines = getLines()
    input = makeInput(lines)
    print(input)


main()
