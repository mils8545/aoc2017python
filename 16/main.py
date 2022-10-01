import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "16"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Instruction:
    def __init__(self, name : str, args : List[str]) -> None:
        self.name : str = name
        self.args : List[str] = args
    def __repr__(self) -> str:
        return f"{self.name} {self.args}"
    def __str__(self) -> str:
        return f"{self.name} {self.args}"

def parseLines(lines : List[str]) -> List[Instruction]:
    instructions : List[Instruction] = []
    for part in lines[0].split(","):
        instructions.append(Instruction(part[0], part[1:].split("/")))
    return instructions

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    instructions : List[Instruction] = parseLines(lines)
    programs : List[str] = [chr(i) for i in range(ord("a"), ord("p")+1)]
    for instruction in instructions:
        if instruction.name == "s":
            programs = programs[-int(instruction.args[0]):] + programs[:-int(instruction.args[0])]
        elif instruction.name == "x":
            programs[int(instruction.args[0])], programs[int(instruction.args[1])] = programs[int(instruction.args[1])], programs[int(instruction.args[0])]
        elif instruction.name == "p":
            aIndex : int = programs.index(instruction.args[0])
            bIndex : int = programs.index(instruction.args[1])
            programs[aIndex], programs[bIndex] = programs[bIndex], programs[aIndex]
    result : str = "".join(programs)

    return f"Password is {result}."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    instructions : List[Instruction] = parseLines(lines)
    programs : List[str] = [chr(i) for i in range(ord("a"), ord("p")+1)]
    stateList : List[str] = []
    runCount : int = 0
    while not ("".join(programs) == "abcdefghijklmnop") or runCount == 0:
        stateList.append("".join(programs))
        for instruction in instructions:
            if instruction.name == "s":
                programs = programs[-int(instruction.args[0]):] + programs[:-int(instruction.args[0])]
            elif instruction.name == "x":
                programs[int(instruction.args[0])], programs[int(instruction.args[1])] = programs[int(instruction.args[1])], programs[int(instruction.args[0])]
            elif instruction.name == "p":
                aIndex : int = programs.index(instruction.args[0])
                bIndex : int = programs.index(instruction.args[1])
                programs[aIndex], programs[bIndex] = programs[bIndex], programs[aIndex]
        runCount += 1

    remainingRuns : int = 1000000000 % runCount
    for i in range(remainingRuns):
        for instruction in instructions:
            if instruction.name == "s":
                programs = programs[-int(instruction.args[0]):] + programs[:-int(instruction.args[0])]
            elif instruction.name == "x":
                programs[int(instruction.args[0])], programs[int(instruction.args[1])] = programs[int(instruction.args[1])], programs[int(instruction.args[0])]
            elif instruction.name == "p":
                aIndex : int = programs.index(instruction.args[0])
                bIndex : int = programs.index(instruction.args[1])
                programs[aIndex], programs[bIndex] = programs[bIndex], programs[aIndex]
    result : str = "".join(programs)
    return f"Password is {result}."

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
    print("Advent of Code 2017 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()