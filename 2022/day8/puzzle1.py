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


def checkVisibility(trees):
    visibleTreeCoordinates = {}

    def checkVisibilityLeft():
        for r in range(0, len(trees)):
            treeLeft = -1
            for c in range(0, len(trees[r])):
                if(trees[r][c] > treeLeft):
                    visibleTreeCoordinates["y:"+str(r) + "x:"+str(c)] = trees[r][c]
                    treeLeft = trees[r][c]

    def checkVisibilityTop():
        for c in range(0, len(trees[0])):
            treeAbove = -1
            for r in range(0, len(trees)):
                if(trees[r][c] > treeAbove):
                    visibleTreeCoordinates["y:"+str(r) + "x:"+str(c)] = trees[r][c]
                    treeAbove = trees[r][c]

    def checkVisibilityRight():
        for r in range(0, len(trees)):
            treeRight = -1
            for c in range(0, len(trees[r])):
                col = len(trees[r]) - 1 - c
                if(trees[r][col] > treeRight):
                    visibleTreeCoordinates["y:"+str(r) + "x:"+str(col)] = trees[r][col]
                    treeRight = trees[r][col]

    def checkVisibilityBottom():
        for c in range(0, len(trees[0])):
            treeUnder = -1
            for r in range(0, len(trees)):
                row = len(trees)-1 - r
                if(trees[row][c] > treeUnder):
                    visibleTreeCoordinates["y:"+str(row) + "x:"+str(c)] = trees[row][c]
                    treeUnder = trees[row][c]

    checkVisibilityBottom()
    checkVisibilityLeft()
    checkVisibilityRight()
    checkVisibilityTop()
    return visibleTreeCoordinates


def main():
    lines = getLines()
    trees = getTrees(lines)
    visibleTrees = checkVisibility(trees)
    print(len(visibleTrees))


main()
