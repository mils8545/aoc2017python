import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "10"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class KnotHash:
    def __init__(self, length : int, lengths : List[int]) -> None:
        self.listSize : int = length
        self.lengths : List[int] = lengths
        self.list : List[int] = [i for i in range(self.listSize)]
        self.currentPosition : int = 0
        self.skipSize : int = 0
    
    def run(self) -> None:
        for length in self.lengths:
            if self.currentPosition + length < self.listSize:
                self.list[self.currentPosition:self.currentPosition+length] = self.list[self.currentPosition:self.currentPosition+length][::-1]
            else:
                tempList : List[int] = self.list[self.currentPosition:] + self.list[:(self.currentPosition+length)%self.listSize]
                tempList = tempList[::-1]
                self.list[self.currentPosition:] = tempList[:self.listSize-self.currentPosition]
                self.list[:(self.currentPosition+length)%self.listSize] = tempList[self.listSize-self.currentPosition:]
            self.currentPosition = (self.currentPosition + length + self.skipSize) % self.listSize
            self.skipSize += 1

def part1(lines : List[str]) -> str:
    lengths : List[int] = [int(num) for num in lines[0].split(",")]
    listSize : int = 256
    list : List[int] = [i for i in range(listSize)]
    skipSize : int = 0
    i : int = 0
    for length in lengths:
        if i + length < listSize:
            list[i:i+length] = list[i:i+length][::-1]
        else:
            tempList : List[int] = list[i:] + list[:(i+length)%listSize]
            tempList = tempList[::-1]
            list[i:] = tempList[:listSize-i]
            list[:(i+length)%listSize] = tempList[listSize-i:]
        i = (i + length + skipSize) % listSize
        skipSize += 1

    return f"{list[0] * list[1]}"

def part2(lines : List[str]) -> str:
    lengths : List[int] = [ord(char) for char in lines[0]] + [17, 31, 73, 47, 23]
    listSize : int = 256
    knotHash : KnotHash = KnotHash(listSize, lengths)
    for i in range(64):
        knotHash.run()
    hexHash : str = ""
    for i in range(16):
        num : int = knotHash.list[i*16]
        for j in range(1,16):
            num ^= knotHash.list[i*16+j]
        hexHash += f"{num:02x}"
    return hexHash

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