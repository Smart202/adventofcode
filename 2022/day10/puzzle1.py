#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def runProgram(lines):
    program = {"cycle": 0, "x": 1}
    sums = []
    totalSum = 0
    def addV(input):
        runCycle()
        runCycle()
        program["x"] += input

    def noop():
        runCycle()

    def runCycle():
        program["cycle"] += 1
        if (program["cycle"] + 20) % 40 == 0:
            sums.append(program["cycle"] * program["x"])
            print("cycle: ",program["cycle"], "x: ",program["x"])

    for line in lines:
        if line.strip() == "noop":
            noop()
        else:
            _, num = line.strip().split(" ")
            addV(int(num))
    for n in range(0, 6):
        totalSum += sums[n]
    return totalSum


def main():
    lines = getLines()
    cyclePoints = runProgram(lines)
    print(cyclePoints)


main()
