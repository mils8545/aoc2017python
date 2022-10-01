import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "06"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def redistribute(banks : List[int]) -> List[int]:
    maxBank : int = 0
    maxBlocks : int = 0
    for i in range(len(banks)):
        if banks[i] > maxBlocks:
            maxBank = i
            maxBlocks = banks[i]

    banks[maxBank] = 0
    for i in range(maxBlocks):
        banks[(maxBank + i + 1) % len(banks)] += 1
    return banks

def part1(lines : List[str]) -> str:
    banks : List[int] = [int(x) for x in lines[0].split("\t")]
    seen : List[str] = []

    while True:
        seen.append(str(banks))
        banks = redistribute(banks)
        if str(banks) in seen:
            return str(len(seen))

def part2(lines : List[str]) -> str:
    banks : List[int] = [int(x) for x in lines[0].split("\t")]
    seen : Dict[str, int] = {}

    while True:
        bankHash : str = str(banks)
        seen[bankHash] = len(seen) + 1
        banks = redistribute(banks)
        if str(banks) in seen:
            bankHash = str(banks)
            return str(len(seen)-seen[bankHash]+1)

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