import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "12"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Node:
    def __init__(self, name : str, connectionList : List[str], connections : List["Node"]) -> None:
        self.name : str = name
        self.connectionList : List[str] = connectionList
        self.connections : List["Node"] = []
    def connectionSet(self, seen : List[str]) -> List[str]:
        seen.append(self.name)
        for connection in self.connections:
            if connection.name not in seen:
                seen = connection.connectionSet(seen)
        return seen        

def parseLines(lines : List[str]) -> Dict[str, Node]:
    nodes : Dict[str, Node] = {}
    for lineString in lines:
        line : List[str] = lineString.split(" <-> ")
        name : str = line[0]
        connectionList : List[str] = line[1].split(", ")
        nodes[name] = Node(name, connectionList, [])
    return nodes

def part1(lines : List[str]) -> str:
    nodes : Dict[str, Node] = parseLines(lines)
    for node in nodes.values():
        for connection in node.connectionList:
            node.connections.append(nodes[connection])
    return f"There are {len(nodes['0'].connectionSet([]))} programs in the group that contains program 0."

def part2(lines : List[str]) -> str:
    nodes : Dict[str, Node] = parseLines(lines)
    for node in nodes.values():
        for connection in node.connectionList:
            node.connections.append(nodes[connection])
    connectedNodes : List[str] = []
    groups : int = 0
    for node in nodes.values():
        if node.name not in connectedNodes:
            connectedNodes += node.connectionSet([])
            groups += 1
    return f"There are {groups} groups in total."

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