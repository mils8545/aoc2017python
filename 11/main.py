import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "11"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class HexPoint:
    def __init__(self, q : int, r : int, s : int) -> None:
        self.q : int = q
        self.r : int = r
        self.s : int = s
    def __add__(self, other : "HexPoint") -> "HexPoint":
        return HexPoint(self.q + other.q, self.r + other.r, self.s + other.s)
    def distance(self, other : Union["HexPoint",None] = None) -> int:
        if other is None:
            other = HexPoint(0,0,0)
        return (abs(self.q - other.q) + abs(self.r - other.r) + abs(self.s - other.s)) // 2

directionHexPoints : Dict[str, HexPoint] = {"n": HexPoint(0,1,-1), "ne": HexPoint(1,0,-1), "se": HexPoint(1,-1,0), "s": HexPoint(0,-1,1), "sw": HexPoint(-1,0,1), "nw": HexPoint(-1,1,0)}

def part1(lines : List[str]) -> str:
    directions : List[str] = lines[0].split(",")
    position : HexPoint = HexPoint(0,0,0)

    for direction in directions:
        position += directionHexPoints[direction]
    return f"The distance is {position.distance()}."

def part2(lines : List[str]) -> str:
    directions : List[str] = lines[0].split(",")
    position : HexPoint = HexPoint(0,0,0)
    furthestDistance : int = 0
    for direction in directions:
        position += directionHexPoints[direction]
        furthestDistance  : int = max(furthestDistance, position.distance())
    return f"The furthest distance was {furthestDistance}."

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