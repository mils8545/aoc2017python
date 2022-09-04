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

class Sensor:
    def __init__ (self, num, length):
        self.num = num
        self.length = length
        self.pos = 0
        self.dir = 1
    def step(self):
        self.pos += self.dir
        if self.pos == self.length - 1 or self.pos == 0:
            self.dir *= -1

def parseLines(lines : List[str]) -> List[Sensor]:
    sensors = []
    for line in lines:
        num, length = line.split(": ")
        sensors.append(Sensor(int(num), int(length)))
    return sensors

def part1(lines : List[str]) -> str:
    sensors = parseLines(lines)
    maxSensor = sensors[-1].num
    severity = 0
    for i in range(maxSensor + 1):
        for sensor in sensors:
            if sensor.num == i:
                if sensor.pos == 0:
                    severity += sensor.num * sensor.length
        for sensor in sensors:
            sensor.step()
    return str(severity)

def part2(lines : List[str]) -> str:
    delay = -1
    while True:
        delay += 1
        sensors = parseLines(lines)
        maxSensor = sensors[-1].num
        caught = False
        for i in range(delay):
            for sensor in sensors:
                sensor.step()
        for i in range(maxSensor + 1):
            for sensor in sensors:
                if sensor.num == i:
                    if sensor.pos == 0:
                        caught = True
                        break
            for sensor in sensors:
                sensor.step()
        if not caught:
            return f"{delay}"

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