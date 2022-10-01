import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "22"

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
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)

def parseLines(lines : List[str]) -> List[str]:
    width : int = len(lines[0])
    height : int = len(lines)
    infected : List[str] = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                infected.append(str(Point(x - width // 2, y - height // 2)))
    return infected

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    infected : List[str] = parseLines(lines)
    DIRECTIONS : List[Point] = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
    direction : int = 0
    position : Point = Point(0, 0)
    count : int = 0

    for i in range(10000):
        if str(position) in infected:
            direction = (direction + 1) % 4
            infected.remove(str(position))
        else:
            direction = (direction - 1) % 4
            infected.append(str(position))
            count += 1
        position += DIRECTIONS[direction]
    return f"There were {count} infections after 10,000 cycles."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    infected : List[str] = parseLines(lines)
    weakened : List[str] = []
    flagged : List[str] = []
    DIRECTIONS : List[Point] = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
    direction : int = 0
    position : Point = Point(0, 0)
    count : int = 0

    for i in range(10000000):
    # for i in range(100):
        # if i % 100000 == 0:
        #     print(i)
        if str(position) in infected:
            direction = (direction + 1) % 4
            flagged.append(str(position))
            infected.remove(str(position))
        elif str(position) in weakened:
            weakened.remove(str(position))
            infected.append(str(position))
            count += 1
        elif str(position) in flagged:
            direction = (direction + 2) % 4
            flagged.remove(str(position))
        else:
            weakened.append(str(position))
            direction = (direction - 1) % 4

        position += DIRECTIONS[direction]
    return f"There were {count} infections after 10,000,000 cycles."

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