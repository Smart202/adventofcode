#!/bin/python


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def makeNodes(lines):
    nodeCols = []
    yCounter = 0
    startCords = False
    endCords = False
    for line in lines:
        xCounter = 0
        nodeRows = []
        for letter in line.strip():
            addAbove = True
            addBellow = True
            addRight = True
            addLeft = True
            if yCounter == 0:
                addAbove = False
            elif yCounter == len(lines) -1:
                addBellow = False
            if xCounter == 0:
                addLeft = False
            elif xCounter == len(line.strip()) -1:
                addRight = False
            node = {
                "letter": letter,
                "value": ord(letter),
                "x": xCounter,
                "y": yCounter,
                "connections": []
            }
            if addAbove :
                node["connections"].append({
                    "x": xCounter,
                    "y": yCounter-1
                })
            if addBellow :
                node["connections"].append({
                    "x": xCounter,
                    "y": yCounter+1
                })
            if addLeft :
                node["connections"].append({
                    "x": xCounter-1,
                    "y": yCounter
                })
            if addRight :
                node["connections"].append({
                    "x": xCounter+1,
                    "y": yCounter
                })
            
            if letter == "S":
                startCords = (xCounter, yCounter)
                node["value"] = ord("a")
                nodeRows.append(node)
            elif letter == "E":
                endCords = (xCounter, yCounter)
                node["value"] = ord("z")
                nodeRows.append(node)
            else:
                nodeRows.append(node)
            xCounter +=1
        
        nodeCols.append(nodeRows)
        yCounter +=1

    
    
    return nodeCols, startCords,endCords


def makeProgram(nodeCols, startCords, endCords):
    shortestFromStart = {}
    visited = []
    que = []
    x,y = startCords
    que.append(str(x)+"-"+str(y))
    shortestFromStart[str(x)+"-"+str(y)] = 0
    while que:
        cordString = que.pop(0)
        print("popped ", cordString, " from que")
        cords = cordString.split("-")
        node = nodeCols[int(cords[1])][int(cords[0])]
        visited.append(cordString)
        for connection in node["connections"]:
            con = nodeCols[connection["y"]][connection["x"]]
            if node["value"]+1 >= con["value"]:
                conString = str(con["x"]) + "-"+str(con['y'])
                if conString not in que and conString not in visited:
                    print("putting ", conString," in que")
                    que.append(conString)
                    shortestFromStart[conString] = shortestFromStart[cordString] +1
                
    x,y = endCords
    return shortestFromStart[str(x)+"-"+str(y)]


def main():
    lines = getLines()
    nodeCols, startCords, endCords = makeNodes(lines)
    program = makeProgram(nodeCols,startCords, endCords)
    print(program)


main()
