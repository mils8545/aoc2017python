import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "14"

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

    def run64(self) -> None:
        for i in range(64):
            self.run()

    def getDenseHash(self) -> List[int]:
        denseHash : List[int] = []
        for i in range(16):
            denseHash.append(self.list[i*16])
            for j in range(1, 16):
                denseHash[i] ^= self.list[i*16+j]
        return denseHash

def byteToBits(byte : int) -> List[bool]:
    bits : List[bool] = []
    for i in range(8):
        bits.append(bool(byte & (1 << i)))
    return bits

def part1(lines : List[str]) -> str:
    salt : str = lines[0]
    gridHash : List[List[int]] = []
    listSize : int = 256

    for i in range(128):
        lengths : List[int] = [ord(char) for char in (f"{salt}-{i}")] + [17, 31, 73, 47, 23]
        knotHash : KnotHash = KnotHash(listSize, lengths)
        knotHash.run64()
        gridHash.append(knotHash.getDenseHash())

    count : int = 0
    grid : List[List[bool]] = []
    for i in range(128):
        grid.append([])
        for byte in gridHash[i]:
            for bit in byteToBits(byte):
                grid[i].append(bit)
    for line in grid:
        for bit in line:
            if bit:
                count += 1

    return f"There are {count} used sectors."

def part2(lines : List[str]) -> str:
    salt : str = lines[0]
    gridHash : List[List[int]] = []
    listSize : int = 256

    for i in range(128):
        lengths : List[int] = [ord(char) for char in (f"{salt}-{i}")] + [17, 31, 73, 47, 23]
        knotHash : KnotHash = KnotHash(listSize, lengths)
        knotHash.run64()
        gridHash.append(knotHash.getDenseHash())

    count : int = 0
    grid : List[List[bool]] = []
    for i in range(128):
        grid.append([])
        for byte in gridHash[i]:
            for bit in byteToBits(byte):
                grid[i].append(bit)
    for line in grid:
        for bit in line:
            if bit:
                count += 1

    return f"Not are {0} regions."

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