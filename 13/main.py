import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "13"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def parseLines(lines : List[str]) -> List[int]:
    maxSensor : int = max([int(line.split(": ")[0]) for line in lines])
    sensors : List[int] = [-1] * (maxSensor + 1)
    for line in lines:
        num : int = int(line.split(": ")[0])
        length : int = int(line.split(": ")[1])
        sensors[num] = (length - 1) * 2
    return sensors

def part1(lines : List[str]) -> str:
    sensors : List[int] = parseLines(lines)
    severity : int = 0
    for i in range(len(sensors)):
        if sensors[i] != -1 and i % sensors[i] == 0:
            severity += i * (sensors[i] // 2 + 1)

    return str(severity)

def part2(lines : List[str]) -> str:
    sensors : List[int] = parseLines(lines)
    delay : int = -1
    while True:
        delay += 1
        caught : bool = False
        for i in range(len(sensors)):
            if sensors[i] != -1 and (i + delay) % sensors[i] == 0:
                caught = True
                break
        if not caught:
            return str(delay)


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