#!/bin/python
import time


def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def makeCommands(lines):
    commands = []
    currentCommand = {"response": []}
    for line in lines:
        line = line.strip()
        if(line[0] == "$"):
            if "command" in currentCommand:
                commands.append(currentCommand)
                currentCommand = {"response": []}
            currentCommand["command"] = line[2:len(line)]
        else:
            currentCommand["response"].append(line)
    commands.append(currentCommand)
    return commands


def makeFileSys(commands):
    dirTree = []
    fileSystem = {"dirs": {}, "totalSize": 0, "sizeExDirs": 0}
    currentDir = fileSystem
    dirTree.append(currentDir)
    for command in commands:
        if command["command"][0:2] == "cd":
            [command, dir] = command["command"].split(" ")
            if(dir == ".."):
                dirTree.pop()
                currentDir = dirTree[-1]
            else:
                if dir not in dirTree[-1]["dirs"]:
                    newFolder = {
                        "files": [], "dirs": {}, "sizeExDirs": 0, "totalSize": 0
                    }
                    currentDir["dirs"][dir] = newFolder
                    currentDir = newFolder
                else:
                    currentDir = dirTree[-1]["dirs"][dir]
                dirTree.append(currentDir)
        elif(command["command"] == "ls"):
            for data in command["response"]:
                [pre, _] = data.split(" ")
                if(pre != "dir"):
                    if data not in currentDir["files"]:
                        currentDir["files"].append(data)
                        currentDir["sizeExDirs"] += int(pre)
    calculateTotalSize(fileSystem)
    return fileSystem


def calculateTotalSize(fileSystem):
    if fileSystem["totalSize"] > 0:
        return fileSystem["totalSize"]
    size = fileSystem["sizeExDirs"]
    for dir in fileSystem["dirs"]:
        size += calculateTotalSize(fileSystem["dirs"][dir])
    fileSystem["totalSize"] = size
    return fileSystem["totalSize"]


def less100k(dirs):
    num = 0
    for dir in dirs:
        if(dirs[dir]["totalSize"] <= 100000):
            num += dirs[dir]["totalSize"]
        num += less100k(dirs[dir]["dirs"])
    return num


def getCode(lines):
    commands = makeCommands(lines)
    fileSystem = makeFileSys(commands)
    filtered = less100k(fileSystem["dirs"])

    return filtered


def main():
    start = time.time()
    lines = getLines()
    msg = getCode(lines)
    print(msg)
    end = time.time()
    runtime = end - start
    runtime = runtime * 1000
    print("Elapsed time: ", runtime, "ms")


main()
