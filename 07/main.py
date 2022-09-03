import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "07"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Node:
    def __init__(self, name: str, weight: int) -> None:
        self.name : str = name
        self.weight : int = weight
        self.children : List[Node] = []
        self.parent : Union [Node, None] = None
    def getWeight(self) -> int:
        weight : int = self.weight
        for child in self.children:
            weight += child.getWeight()
        return weight
    def balanced(self) -> bool:
        if len(self.children) == 0:
            return True
        weights : List[int] = [child.getWeight() for child in self.children]
        return weights.count(weights[0]) == len(weights)

class NodeInfo:
    def __init__(self, name: str, weight: int, children: List[str]) -> None:
        self.name : str = name
        self.weight : int = weight
        self.children : List[str] = children
    def __str__(self) -> str:
        return f"NodeInfo({self.name}, {self.weight}, {self.children})"

def parseLines (lines : List[str]) -> List[NodeInfo]:
    nodes : List[NodeInfo] = []
    for lineString in lines:
        line : List[str] = lineString.split("->")
        name : str = line[0].split(" ")[0]
        weight : int = int(line[0].split(" ")[1].strip("()"))
        children : List[str] = []
        if len(line) > 1:
            children = line[1][1:].split(", ")
        nodes.append(NodeInfo(name, weight, children))
    return nodes

def part1(lines : List[str]) -> str:
    nodeInfoList : List[NodeInfo] = parseLines(lines)
    nodeDict : Dict[str, Node] = {}
    for nodeInfo in nodeInfoList:
        nodeDict[nodeInfo.name] = Node(nodeInfo.name, nodeInfo.weight)
    for nodeInfo in nodeInfoList:
        for child in nodeInfo.children:
            nodeDict[nodeInfo.name].children.append(nodeDict[child])
            nodeDict[child].parent = nodeDict[nodeInfo.name]
    tree : Union[Node, None] = None

    for node in nodeDict.values():
        if node.parent == None:
            tree = node
            break
    if tree == None:
        return "ERROR: No root node found."
    else:
        return f"The base of the tower is {tree.name}."

def part2(lines : List[str]) -> str:
    nodeInfoList : List[NodeInfo] = parseLines(lines)
    nodeDict : Dict[str, Node] = {}
    for nodeInfo in nodeInfoList:
        nodeDict[nodeInfo.name] = Node(nodeInfo.name, nodeInfo.weight)
    for nodeInfo in nodeInfoList:
        for child in nodeInfo.children:
            nodeDict[nodeInfo.name].children.append(nodeDict[child])
            nodeDict[child].parent = nodeDict[nodeInfo.name]
    tree : Union[Node, None] = None

    for node in nodeDict.values():
        if node.parent == None:
            tree = node
            break

    if tree == None:
        return "ERROR: No root node found."

    def findUnbalanced(node : Node) -> Union[Node, None]:
        if not node.balanced():
            for child in node.children:
                if not child.balanced():
                    return findUnbalanced(child)
            return node
        return None

    unbalanced : Union[Node, None] = findUnbalanced(tree)

    if unbalanced == None:
        return "ERROR: No unbalanced node found."

    from collections import Counter
 
    occurence_count : Counter[int] = Counter([child.getWeight() for child in unbalanced.children])
    incorrectWeight : int = occurence_count.most_common()[-1][0]
    correctWeight : int = occurence_count.most_common()[0][0]

    for child in unbalanced.children:
        if child.getWeight() == incorrectWeight:
            return f"The correct weight of {child.name} is {child.weight + correctWeight - incorrectWeight}."

    return "ERROR: No unbalanced node found."

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