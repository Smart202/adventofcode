#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def getTrees(lines):
    trees = []
    for line in lines:
        row = []
        for char in line.strip():
            row.append(int(char))
        trees.append(row)
    return trees


def checkBestSpot(trees):
    bestSpotValue = 0

    def calculateHouseValue(row, col, showResult=False):
        height = trees[row][col]
        l, u, r, d = 0, 0, 0, 0
        for y in range(1, col + 1):
            l += 1
            if trees[row][col - y] >= height:
                break
        for x in range(1, row + 1):
            u += 1
            if trees[row - x][col] >= height:
                break
        for y in range(col + 1, len(trees[0])):
            r += 1
            if trees[row][y] >= height:
                break
        for x in range(row+1, len(trees)):
            d += 1
            if(trees[x][col] >= height):
                break
        if(showResult):
            print("trees[", row, "][", col, "] with height: ",
                  height, " get values :")
            print("l: ", l, " - u: ", u, " - r: ", r, " - d: ", d)
            print("score: ", l * u * r * d)
        return l * u * r * d

    for r in range(0, len(trees)):
        for c in range(0, len(trees[r])):
            value = calculateHouseValue(r, c)
            if(value > bestSpotValue):
                print("NEW LEADER")
                calculateHouseValue(r, c, True)
                bestSpotValue = value

    return bestSpotValue


def main():
    lines = getLines()
    trees = getTrees(lines)
    bestSpotValue = checkBestSpot(trees)
    print(bestSpotValue)


main()
