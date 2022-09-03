import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "08"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Instruction:
    def __init__(self, reg, op, val, condReg, condOp, condVal) -> None:
        self.reg = reg
        self.op = op
        self.val = val
        self.condReg = condReg
        self.condOp = condOp
        self.condVal = condVal
    def __str__(self) -> str:
        return f"Instruction({self.reg}, {self.op}, {self.val}, {self.condReg}, {self.condOp}, {self.condVal})"
    # c inc -20 if c == 10

def parseLines (lines : List[str]) -> List[Instruction]:
    instructions : List[Instruction] = []
    for lineString in lines:
        line : List[str] = lineString.split(" ")
        reg : str = line[0]
        op : str = line[1]
        val : int = int(line[2])
        condReg : str = line[4]
        condOp : str = line[5]
        condVal : int = int(line[6])
        instructions.append(Instruction(reg, op, val, condReg, condOp, condVal))
    return instructions

def part1(lines : List[str]) -> str:
    instructions : List[Instruction] = parseLines(lines)
    registers : dict[str, int] = {}
    for instruction in instructions:
        if instruction.reg not in registers:
            registers[instruction.reg] = 0
        if instruction.condReg not in registers:
            registers[instruction.condReg] = 0

    opDict : dict[str, int] = {"inc": 1, "dec": -1}

    for instruction in instructions:
        if instruction.condOp == "==":
            if registers[instruction.condReg] == instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "!=":
            if registers[instruction.condReg] != instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == ">":
            if registers[instruction.condReg] > instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "<":
            if registers[instruction.condReg] < instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == ">=":
            if registers[instruction.condReg] >= instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "<=":
            if registers[instruction.condReg] <= instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        else:
            print("ERROR: Invalid operator: " + instruction.condOp)
            return "ERROR"

    maxVal : int = -20000
    for key in registers:
        if registers[key] > maxVal:
            maxVal = registers[key]

    return f"The highest value in any register is {maxVal}."

def part2(lines : List[str]) -> str:
    instructions : List[Instruction] = parseLines(lines)
    registers : dict[str, int] = {}
    maxVal : int = -20000

    for instruction in instructions:
        if instruction.reg not in registers:
            registers[instruction.reg] = 0
        if instruction.condReg not in registers:
            registers[instruction.condReg] = 0

    opDict : dict[str, int] = {"inc": 1, "dec": -1}

    for instruction in instructions:
        if instruction.condOp == "==":
            if registers[instruction.condReg] == instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "!=":
            if registers[instruction.condReg] != instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == ">":
            if registers[instruction.condReg] > instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "<":
            if registers[instruction.condReg] < instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == ">=":
            if registers[instruction.condReg] >= instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        elif instruction.condOp == "<=":
            if registers[instruction.condReg] <= instruction.condVal:
                registers[instruction.reg] += instruction.val * opDict[instruction.op]
        else:
            print("ERROR: Invalid operator: " + instruction.condOp)
            return "ERROR"
        if registers[instruction.reg] > maxVal:
            maxVal = registers[instruction.reg]

    return f"The highest value in any register is {maxVal}."

def main () -> None:
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName : Union[List[str], str, None] = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
        return
    if isinstance(fileName, list):
        print("ERROR: Script can only take one file.")
        return
    lines: List[str] = readFile(fileName)
    p1StartTime: float = time.perf_counter()
    p1Result: str = part1(lines)
    p1EndTime: float = time.perf_counter()
    p2StartTime: float = time.perf_counter()
    p2Result: str = part2(lines)
    p2EndTime: float = time.perf_counter()
    print("Advent of Code 2019 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()