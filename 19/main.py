import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "19"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x : int = x
        self.y : int = y
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)

def part1(lines : List[str]) -> str:
    maxLine: int = 0
    for line in lines:
        if len(line) > maxLine:
            maxLine = len(line)
    maxLine += 1
    grid: List[List[str]] = []
    for i in range(len(lines)):
        grid.append([])
        for j in range(maxLine):
            if j < len(lines[i]):
                grid[i].append(lines[i][j])
            else:
                grid[i].append(" ")
    position : Point = Point(lines[0].find("|"), -1)
    DIRECTIONS : List[Point] = [Point(0,1), Point(1,0), Point(0,-1), Point(-1,0)]
    direction : int = 0
    letters : str = ""
    steps : int = 0
    while True:
        position += DIRECTIONS[direction]
        steps += 1
        if grid[position.y][position.x] == "+":
            if direction == 0 or direction == 2:
                if grid[position.y][position.x + 1] != " ":
                    direction = 1
                else:
                    direction = 3
            else:
                if grid[position.y + 1][position.x] != " ":
                    direction = 0
                else:
                    direction = 2
        elif grid[position.y][position.x].isalpha():
            letters += lines[position.y][position.x]
            nextPos : Point = position + DIRECTIONS[direction]
            if grid[nextPos.y][nextPos.x] == " ":
                return f"The letters in order is {letters}."

def part2(lines : List[str]) -> str:
    maxLine: int = 0
    for line in lines:
        if len(line) > maxLine:
            maxLine = len(line)
    maxLine += 1
    grid: List[List[str]] = []
    for i in range(len(lines)):
        grid.append([])
        for j in range(maxLine):
            if j < len(lines[i]):
                grid[i].append(lines[i][j])
            else:
                grid[i].append(" ")
    position : Point = Point(lines[0].find("|"), -1)
    DIRECTIONS : List[Point] = [Point(0,1), Point(1,0), Point(0,-1), Point(-1,0)]
    direction : int = 0
    letters : str = ""
    steps : int = 0
    while True:
        position += DIRECTIONS[direction]
        steps += 1
        if grid[position.y][position.x] == "+":
            if direction == 0 or direction == 2:
                if grid[position.y][position.x + 1] != " ":
                    direction = 1
                else:
                    direction = 3
            else:
                if grid[position.y + 1][position.x] != " ":
                    direction = 0
                else:
                    direction = 2
        elif grid[position.y][position.x].isalpha():
            letters += lines[position.y][position.x]
            nextPos : Point = position + DIRECTIONS[direction]
            if grid[nextPos.y][nextPos.x] == " ":
                return f"It takes {steps} steps to get to the end."

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