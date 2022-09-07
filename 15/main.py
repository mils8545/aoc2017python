import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "15"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    aCurrent : int = int(lines[0].split(" ")[4])
    bCurrent : int = int(lines[1].split(" ")[4])
    aFactor : int = 16807
    bFactor : int = 48271
    divisor : int = 2147483647
    count : int = 0
    for i in range(40000000):
        aCurrent = (aCurrent * aFactor) % divisor
        bCurrent = (bCurrent * bFactor) % divisor
        if aCurrent & 0xFFFF == bCurrent & 0xFFFF:
            count += 1
    return f"The judge gave a score of {str(count)}"

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    aCurrent : int = int(lines[0].split(" ")[4])
    bCurrent : int = int(lines[1].split(" ")[4])
    aFactor : int = 16807
    bFactor : int = 48271
    divisor : int = 2147483647

    aList : List[int] = []
    bList : List[int] = []
    while len(aList) < 5000000:
        aCurrent = (aCurrent * aFactor) % divisor
        if aCurrent % 4 == 0:
            aList.append(aCurrent)
    while len(bList) < 5000000:
        bCurrent = (bCurrent * bFactor) % divisor
        if bCurrent % 8 == 0:
            bList.append(bCurrent)

    count : int = 0
    for i in range(5000000):
        if aList[i] & 0xFFFF == bList[i] & 0xFFFF:
            count += 1
    return f"The judge gave a score of {str(count)}"

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