import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "24"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Port:
    def __init__(self, input: int, output: int) -> None:
        self.input : int = input
        self.output : int = output
    def __str__(self) -> str:
        return f"{self.input}/{self.output}"
    def __eq__(self, other) -> bool:
        return self.input == other.input and self.output == other.output
    def value(self) -> int:
        return self.input + self.output

class Chain():
    def __init__(self, next: int, ports: List[Port]) -> None:
        self.next : int = next
        self.portList : List[Port] = ports
    def __str__(self) -> str:
        return f"{self.next} {self.value()}"
    def value(self) -> int:
        return sum(port.value() for port in self.portList)

def findHighestValueChain(currentChain : Chain, ports: List[Port]) -> Chain:
    bestChain : Chain = Chain(currentChain.next, currentChain.portList)
    for port in ports:
        if port.input == currentChain.next or port.output == currentChain.next:
            next : int = -9999999
            if port.input == currentChain.next:
                next = port.output
            else:
                next = port.input
            newChain : Chain = Chain(next, currentChain.portList.copy())
            newChain.portList.append(port)
            newPorts : List[Port] = ports.copy()
            newPorts.remove(port)
            newChain = findHighestValueChain(newChain, newPorts)
            if newChain.value() > bestChain.value():
                bestChain = newChain
    return bestChain

def findLongestChain(currentChain : Chain, ports: List[Port]) -> Chain:
    bestChain : Chain = Chain(currentChain.next, currentChain.portList)
    for port in ports:
        if port.input == currentChain.next or port.output == currentChain.next:
            next : int = -9999999
            if port.input == currentChain.next:
                next = port.output
            else:
                next = port.input
            newChain : Chain = Chain(next, currentChain.portList.copy())
            newChain.portList.append(port)
            newPorts : List[Port] = ports.copy()
            newPorts.remove(port)
            newChain = findLongestChain(newChain, newPorts)
            if len(newChain.portList) > len(bestChain.portList):
                bestChain = newChain
            elif len(newChain.portList) == len(bestChain.portList):
                if newChain.value() > bestChain.value():
                    bestChain = newChain
    return bestChain

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    ports : List[Port] = []
    for line in lines:
        ports.append(Port(int(line.split("/")[0]), int(line.split("/")[1])))
    chain : Chain = Chain(0, [])
    chain : Chain = findHighestValueChain(chain, ports)
    return f"The highest value port chain is {chain.value()}."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    ports : List[Port] = []
    for line in lines:
        ports.append(Port(int(line.split("/")[0]), int(line.split("/")[1])))
    chain : Chain = Chain(0, [])
    chain : Chain = findLongestChain(chain, ports)
    return f"The longest chain with the highest value has a value of {chain.value()}."

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