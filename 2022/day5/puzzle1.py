#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def makeMatrix(lines):
    separator = 0
    matrix = {
    }
    for row in lines:
        matrixCounter = 0
        separator += 1
        if row == "\n":
            break
        elif(row[0:3] == " 1 "):
            break
        while True:
            start = matrixCounter * 3 + matrixCounter
            end = start + 3
            if(end > len(row)):
                break
            col = row[start:end]
            matrixCounter += 1
            if(col != "   "):
                if matrixCounter in matrix:
                    matrix[matrixCounter] = [col, *matrix[matrixCounter]]
                else:
                    matrix[matrixCounter] = [col]
    separator+=1
    return separator, matrix

def move(matrix, amount, fr, to):
    for i in range(0, amount):
        matrix[to].append(matrix[fr].pop())

def getCode(lines):
    separator, matrix = makeMatrix(lines)
    message = ""
    for line in lines[separator:]:
        row = line.strip().split(' ')
        move(matrix, int(row[1]), int(row[3]), int(row[5]))

    for num in range(1, len(matrix) +1 ):
        message += matrix[num].pop()
    return message


def main():
    lines = getLines()
    msg = getCode(lines)
    print(msg)


main()
