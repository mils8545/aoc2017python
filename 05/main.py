import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "05"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines : List[str]) -> str:
    offsets : List[int] = [int(line) for line in lines]
    pos : int = 0
    steps : int = 0
    while pos >= 0 and pos < len(offsets):
        steps += 1
        offset : int = offsets[pos]
        offsets[pos] += 1
        pos += offset

    return f"The number of steps required to escape the jumps instructions is {steps}."

def part2(lines : List[str]) -> str:
    offsets : List[int] = [int(line) for line in lines]
    pos : int = 0
    steps : int = 0
    while pos >= 0 and pos < len(offsets):
        steps += 1
        offset : int = offsets[pos]
        if offset >= 3:
            offsets[pos] -= 1
        else:
            offsets[pos] += 1
        pos += offset

    return f"The number of steps required to escape the jumps instructions is {steps}."

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