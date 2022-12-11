#!/bin/python

def getLines():
    lines = []
    with open('input.txt') as f:
        lines = f.readlines()
    return lines


def buildProgram(lines):
    monkeys = []
    monkey = {}
    counter = 0
    for line in lines:
        if counter == 0:
            counter+=1
            continue
        line = line.strip()
        if counter == 1:
            monkey["activity"] = 0
            line = line.strip("Starting items: ")
            items = line.split(",")
            monkey["items"] = []
            for item in items:
                monkey["items"].append(int(item.strip()))
        elif counter == 2:
            line = line.strip("Operation: new = ")
            operation = line.split(" ")
            monkey["operation"] = operation
        elif counter == 3:
            line = line.strip("Test: divisible by ")
            monkey["test"] = int(line)
        elif counter == 4:
            line = line.strip("If true: throw to monkey ")
            monkey["true"] = int(line)
        elif counter == 5:
            line = line.strip("If false: throw to monkey ")
            monkey["false"] = int(line)
            monkeys.append(monkey)
            monkey = {}
        elif counter == 6:
            counter = 0
            continue
        counter+=1
    return monkeys


def calculateWorry(old, operands):
    value = old if operands[2] == "old" else int(operands[2])
    if operands[1] == "+":
        return old + value
    elif operands[1] == "*":
        return old * value
    print("ERROR")
    return 0

def runProgram(program):
    for _ in range(0,20):
        for monkey in program:
            while len(monkey["items"]) != 0:
                item = monkey["items"].pop(0)
                monkey["activity"] +=1
                item = calculateWorry(item, monkey["operation"])
                divisionRound = item % 3
                item -= divisionRound
                item = item / 3
                if item % monkey["test"] == 0:
                    program[monkey["true"]]["items"].append(item / monkey["test"])
                else:
                    program[monkey["false"]]["items"].append(item)
    
    activeMonkey1 = 0
    activeMonkey2 = 0
    for monkey in program:
        if monkey["activity"] > activeMonkey1:
            activeMonkey2 = activeMonkey1
            activeMonkey1 = monkey["activity"]
        elif monkey["activity"] > activeMonkey2:
            activeMonkey2 = monkey["activity"]

    return activeMonkey2 * activeMonkey1
            


def main():
    lines = getLines()
    monkeys = buildProgram(lines)
    p = runProgram(monkeys)
    print(p)

main()
