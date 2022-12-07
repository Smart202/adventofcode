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
    folder = {
        "name": "filesystem",
        "parent": False,
        "folders": [],
        "files": [],
        "size": 0,
    }
    base = folder
    for command in commands:
        if command["command"][0:2] == "cd":
            [command, dir] = command["command"].split(" ")
            if(dir == ".."):
                folder = folder["parent"]
            else:
                newFolder = {
                    "name": dir,
                    "parent": folder,
                    "folders": [],
                    "files": [],
                    "size": 0,
                }
                folder["folders"].append(newFolder)
                folder = newFolder
        elif(command["command"] == "ls"):
            containFolders = False
            for data in command["response"]:
                [pre, _] = data.split(" ")
                if(pre != "dir"):
                    if data not in folder["files"]:
                        folder["files"].append(data)
                        folder["size"] += int(pre)
                else:
                    containFolders = True
            if not containFolders:
                plusParent(folder["parent"], folder["size"])

    return base


def plusParent(folder, size):
    folder["size"] += size
    if(folder["parent"]):
        plusParent(folder["parent"], folder["size"])


def less100k(fileSystem):
    num = 0
    for folder in fileSystem:
        if(folder["size"] <= 100000):
            num += folder["size"]
        num += less100k(folder["folders"])
    return num


def getCode(lines):
    commands = makeCommands(lines)
    fileSystem = makeFileSys(commands)
    filtered = less100k(fileSystem["folders"])
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
