#!/bin/python

def getLines():
    lines = []
    with open('test.txt') as f:
        lines = f.readlines()
    return lines


def walkTheTalk(lines):
    walkedPoints = {"x0y0": True}

    def saveCords(x, y):
        walkedPoints["x"+str(x)+"y"+str(y)] = True
    line = {}
    for index in range(0, 10):
        line[index] = {"x": 0, "y": 0}

    def stepWalk(DIR, piece):
        headX = line[piece]["x"]
        headY = line[piece]["y"]
        tailX = line[piece+1]["x"] if piece < 9 else headX
        tailY = line[piece+1]["y"] if piece < 9 else headY
        if DIR == "L":
            if tailX > headX:
                stepWalk("L", piece+1)
                if tailY > headY:
                    stepWalk("D", piece+1)
                elif tailY < headY:
                    stepWalk("U", piece+1)
            headX -= 1
        elif DIR == "U":
            if headY > tailY:
                stepWalk("U", piece+1)
                if tailX > headX:
                    stepWalk("L", piece+1)
                elif tailX < headX:
                    stepWalk("R", piece+1)
            headY += 1
        elif DIR == "R":
            if headX > tailX:
                stepWalk("R", piece+1)
                if tailY > headY:
                    stepWalk("D", piece+1)
                elif tailY < headY:
                    stepWalk("U", piece+1)
            headX += 1
        elif DIR == "D":
            if tailY > headY:
                stepWalk("D", piece+1)
                if tailX > headX:
                    stepWalk("L", piece+1)
                elif tailX < headX:
                    stepWalk("R", piece+1)
            headY -= 1
        
        line[piece]["x"] = headX
        line[piece]["y"] = headY

    for row in lines:
        direction, steps = row.strip().split(" ")
        print(direction, steps)
        for _ in range(0, int(steps)):
            stepWalk(direction, 1)
            saveCords(line[9]["x"], line[9]["y"])
            print("#head", line[0])
            print("#1", line[1])
            print("#2", line[2])
            print("#3", line[3])
            print("#4", line[4])
            
    return walkedPoints


def main():
    lines = getLines()
    walkedPoints = walkTheTalk(lines)
    print(len(walkedPoints))


main()
