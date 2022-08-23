from fileinput import filename
from types import NoneType
import easygui
import time
from itertools import permutations 
from typing import List
from typing import Union


AOCDAY: str = "02"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines: List[str]) -> List[List[int]]:
    cells : List[List[int]] = [[int(x) for x in line.split("\t") if x != ""] for line in lines]
    return cells

def evenDivision(num1: int, num2: int) -> int:
    if num2 < num1:
        num1, num2 = num2, num1
    if num2 % num1 == 0:
        return num2 // num1
    else:
        return 0

def part1(lines) -> str:
    checksum : List[List[int]] = sum([max(line) - min(line) for line in parseLines(lines)])
    return f"The captcha solution is {checksum}."

def part2(lines) -> str:
    cells : List[List[int]] = parseLines(lines)
    total : int = 0
    for line in cells:
        perms = permutations(line)
        for perm in perms:
            total += evenDivision(perm[0], perm[1])
    return f"The captcha solution is {total}."

def main ():
    # Opens a dialog to select the input file
    # Times and runs both solutions
    # Prints the results
    fileName: Union[str,None] = easygui.fileopenbox(default=f"./"+AOCDAY+"/"+"*.txt")
    if fileName == None:
        print("ERROR: No file selected.")
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