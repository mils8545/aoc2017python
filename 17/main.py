import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "17"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Node:
    def __init__(self, value : int, prev : Union["Node", None], next : Union["Node", None]) -> None:
        if next == None:
            next = self
        if prev == None:
            prev = self
        self.value : int = value
        self.next : Node = next
        self.prev : Node = prev
    def insertAfter(self, value : int) -> "Node":
        newNode : Node = Node(value, self, self.next)
        self.next.prev = newNode
        self.next = newNode
        return newNode

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    stepSize : int = int(lines[0])
    nodeList : List[Node] = [Node(0, None, None)]
    nodeList[0].next = nodeList[0]
    nodeList[0].prev = nodeList[0]
    currentNode : Node = nodeList[0]

    for i in range(1, 2018):
        for j in range(stepSize):
            currentNode = currentNode.next
        newNode : Node = currentNode.insertAfter(i)
        currentNode = newNode
        nodeList.append(newNode)

    currentNode = nodeList[0]
    for node in nodeList:
        currentNode = currentNode.next

    return f"The next value after 2017 is {nodeList[-1].next.value}."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    stepSize : int = int(lines[0])
    nodeList : List[Node] = [Node(0, None, None)]
    nodeList[0].next = nodeList[0]
    nodeList[0].prev = nodeList[0]
    currentNode : Node = nodeList[0]

    for i in range(1, 50000001):
        if i % 1000000 == 0:
            print(i)
        for j in range(stepSize):
            currentNode = currentNode.next
        newNode : Node = currentNode.insertAfter(i)
        currentNode = newNode
        nodeList.append(newNode)

    currentNode = nodeList[0]
    for node in nodeList:
        currentNode = currentNode.next

    return f"The next value after 0 after 50000000 iterations is {nodeList[0].next.value}."

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