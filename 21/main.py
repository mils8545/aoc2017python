import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "21"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines : List[str]) -> Dict[str, str]:
    rules : Dict[str, str] = {}
    for line in lines:
        rules[line.split(" ")[0].replace("/", "")] = line.split(" ")[2].replace("/", "")
    return rules

def rotateRight(rule : str) -> str:
    if len(rule) == 4:
        return rule[2] + rule[0] + rule[3] + rule[1]
    else:
        return rule[6] + rule[3] + rule[0] + rule[7] + rule[4] + rule[1] + rule[8] + rule[5] + rule[2]

def flipHorizontal(rule : str) -> str:
    if len(rule) == 4:
        return rule[1] + rule[0] + rule[3] + rule[2]
    else:
        return rule[2] + rule[1] + rule[0] + rule[5] + rule[4] + rule[3] + rule[8] + rule[7] + rule[6]

def findMatch(rule : str, rules : Dict[str, str]) -> str:
    for i in range(4):
        if rule in rules:
            return rules[rule]
        rule = rotateRight(rule)
    rule = flipHorizontal(rule)
    for i in range(4):
        if rule in rules:
            return rules[rule]
        rule = rotateRight(rule)
    return "ERROR: No match found"

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    rules : Dict[str, str] = parseLines(lines)
    grid : List[str] = [".#.", "..#", "###"]

    for iteration in range(5):
        newGrid : List[str] = []
        if len(grid) % 2 == 0:
            size : int = 2
            newSize : int = 3
        else:
            size : int = 3
            newSize : int = 4
        for i in range(len(grid)//size * newSize):
            newGrid.append("")
        for i in range(len(grid)//size):
            for j in range(len(grid)//size):
                rule : str = ""
                if size == 2:
                    rule = grid[i*2][j*2] + grid[i*2][j*2+1] + grid[i*2+1][j*2] + grid[i*2+1][j*2+1]
                else:
                    rule = grid[i*3][j*3] + grid[i*3][j*3+1] + grid[i*3][j*3+2] + grid[i*3+1][j*3] + grid[i*3+1][j*3+1] + grid[i*3+1][j*3+2] + grid[i*3+2][j*3] + grid[i*3+2][j*3+1] + grid[i*3+2][j*3+2]
                newRule : str = findMatch(rule, rules)
                for k in range(newSize):
                    newGrid[i*newSize+k] += newRule[k*newSize:k*newSize+newSize]
        grid = newGrid
    onCount : int = 0
    for line in grid:
        onCount += line.count("#")
    return f"After 5 iterations there are {onCount} pixels on."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    rules : Dict[str, str] = parseLines(lines)
    grid : List[str] = [".#.", "..#", "###"]

    for iteration in range(18):
        newGrid : List[str] = []
        if len(grid) % 2 == 0:
            size : int = 2
            newSize : int = 3
        else:
            size : int = 3
            newSize : int = 4
        for i in range(len(grid)//size * newSize):
            newGrid.append("")
        for i in range(len(grid)//size):
            for j in range(len(grid)//size):
                rule : str = ""
                if size == 2:
                    rule = grid[i*2][j*2] + grid[i*2][j*2+1] + grid[i*2+1][j*2] + grid[i*2+1][j*2+1]
                else:
                    rule = grid[i*3][j*3] + grid[i*3][j*3+1] + grid[i*3][j*3+2] + grid[i*3+1][j*3] + grid[i*3+1][j*3+1] + grid[i*3+1][j*3+2] + grid[i*3+2][j*3] + grid[i*3+2][j*3+1] + grid[i*3+2][j*3+2]
                newRule : str = findMatch(rule, rules)
                for k in range(newSize):
                    newGrid[i*newSize+k] += newRule[k*newSize:k*newSize+newSize]
        grid = newGrid
    onCount : int = 0
    for line in grid:
        onCount += line.count("#")
    return f"After 18 iterations there are {onCount} pixels on."

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