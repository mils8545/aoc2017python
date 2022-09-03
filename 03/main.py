import easygui
import time
import math
from typing import List
from typing import Union

AOCDAY: str = "03"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Point:
    def __init__(self, x : int, y : int) -> None:
        self.x : int = x
        self.y : int = y
    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    def manhattan(self, offset) -> int:
        return abs(self.x - offset.x) + abs(self.y - offset.y)

directions : List[Point] = [Point(1, 0), Point(0, -1), Point(-1, 0), Point(0, 1)]

adjacent : List[Point] = [Point(1, 0), Point(1, -1), Point(0, -1), Point(-1, -1), Point(-1, 0), Point(-1, 1), Point(0, 1), Point(1, 1)]

def part1(lines : List[str]) -> str:
    target : int = int(lines[0])
    ring : int = math.ceil((math.sqrt(target)-1)/2) + 1
    grid : List[List[int]] = [[0 for i in range(2*ring+1)] for j in range(2*ring+1)]
    direction : int = 0
    pos : Point = Point(ring, ring) + directions[direction+2]

    for i in range(1, target+1):
        pos = pos + directions[direction]
        grid[pos.y][pos.x] = i
        turnPoint : Point = pos + directions[(direction + 1) % 4]
        if grid[turnPoint.y][turnPoint.x] == 0:
            direction = (direction + 1) % 4

    return f"The distance to the center is {pos.manhattan(Point(ring, ring))}."

def part2(lines : List[str]) -> str:
    target : int = int(lines[0])
    ring : int = 20
    grid : List[List[int]] = [[0 for i in range(2*ring+1)] for j in range(2*ring+1)]
    direction : int = 1
    pos : Point = Point(ring, ring)
    grid[pos.y][pos.x] = 1

    while True:
        pos = pos + directions[direction]
        grid[pos.y][pos.x] = sum([grid[pos.y + a.y][pos.x + a.x] for a in adjacent])
        if grid[pos.y][pos.x] > target:
            return f"The first value larger than the target is {grid[pos.y][pos.x]}."
        turnPoint : Point = pos + directions[(direction + 1) % 4]
        if grid[turnPoint.y][turnPoint.x] == 0:
            direction = (direction + 1) % 4

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