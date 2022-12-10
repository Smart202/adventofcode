#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def walkTheTalk(lines):
    walkedPoints = {"x0y0": True}

    def saveCords(x, y):
        key = "x"+str(x)+"y"+str(y)
        if key not in walkedPoints:
            print("xy", x, y)
            walkedPoints["x"+str(x)+"y"+str(y)] = True
    line = {}
    for index in range(0, 10):
        line[index] = {"x": 0, "y": 0}

    def stepWalk(piece):
        if(piece >= len(line)):
            return
        xPosToHead = line[piece]["x"] - line[piece - 1]["x"]
        yPosToHead = line[piece]["y"] - line[piece - 1]["y"]
        changeX = -2 >= yPosToHead or yPosToHead >=2
        changeY = (-2 >= xPosToHead or xPosToHead >=2)
        if (changeX) and (changeY):
            line[piece]["x"] += int(xPosToHead/2) * (-1)
            line[piece]["y"] += int(yPosToHead/2) * (-1)
            stepWalk(piece +1)
        elif changeX:
            line[piece]["y"] += int(yPosToHead/2) * (-1)
            if -1 >= xPosToHead or xPosToHead >= 1:
                line[piece]["x"] += xPosToHead * (-1)
            stepWalk(piece +1)
        elif changeY:
            line[piece]["x"] += int(xPosToHead/2) * (-1)
            if -1 >= yPosToHead or yPosToHead >= 1:
                line[piece]["y"] += yPosToHead * (-1)
            stepWalk(piece +1)
     
        return
    for row in lines:
        direction, steps = row.strip().split(" ")
        for _ in range(0, int(steps)):
            if direction == "L":
                line[0]["x"] -= 1
            elif direction == "U":
                line[0]["y"] += 1
            elif direction == "R":
                line[0]["x"] += 1
            elif direction == "D":
                line[0]["y"] -= 1
            stepWalk(1)
            saveCords(line[len(line) - 1]["x"], line[len(line) - 1]["y"])

    return walkedPoints

def main():
    lines = getLines()
    walkedPoints = walkTheTalk(lines)
    print(len(walkedPoints))


main()
