#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def walkTheTalk(lines):
    walkedPoints = {"x0y0": True}
    def saveCords(x,y):
        walkedPoints["x"+str(x)+"y"+str(y)] = True
        
    headX,headY = 0,0
    tailX,tailY = 0,0
    for line in lines:
        direction, steps = line.strip().split(" ")
        for _ in range(0, int(steps)):
            if direction == "L":
                if tailX > headX:
                    tailX -=1
                    if tailY>headY:
                        tailY-=1
                    elif tailY<headY:
                        tailY+=1
                    saveCords(tailX, tailY)
                headX -=1
            elif direction == "U":
                if headY > tailY:
                    tailY +=1
                    if tailX>headX:
                        tailX-=1
                    elif tailX<headX:
                        tailX+=1
                    saveCords(tailX, tailY)
                headY +=1
            elif direction == "R":
                if headX > tailX:
                    tailX +=1
                    if tailY>headY:
                        tailY-=1
                    elif tailY<headY:
                        tailY+=1
                    saveCords(tailX, tailY)
                headX +=1
            elif direction == "D":
                if tailY > headY:
                    tailY -=1
                    if tailX>headX:
                        tailX-=1
                    elif tailX<headX:
                        tailX+=1
                    saveCords(tailX, tailY)
                headY -=1
    return walkedPoints



def main():
    lines = getLines()
    walkedPoints = walkTheTalk(lines)
    print(len(walkedPoints))


main()
