#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def runProgram(lines):
    program = {"cycle": 0, "x": 1, "currentLine": ""}
    screen = []
    def addV(input):
        runCycle()
        runCycle()
        program["x"] += input

    def noop():
        runCycle()

    def addToLine():
        currentPointer = [program["x"] -1, program["x"], program["x"] +1]
        if  len(program["currentLine"]) in currentPointer:
            program["currentLine"]+="#"
        else:
            program["currentLine"]+="."
            
        #print(program["currentLine"])

    def runCycle():
        addToLine()
        program["cycle"] += 1
        if (program["cycle"]) % 40 == 0:
            screen.append(program["currentLine"])
            program["currentLine"] = ""

    for line in lines:
        if line.strip() == "noop":
            noop()
        else:
            _, num = line.strip().split(" ")
            addV(int(num))
    
    for row in screen:
        print(row)


def main():
    lines = getLines()
    cyclePoints = runProgram(lines)


main()
