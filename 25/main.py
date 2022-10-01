import easygui
import time
from typing import List
from typing import Dict
from typing import Union

AOCDAY: str = "25"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class TuringSet:
    def __init__(self, write : int, move : int, next : str) -> None:
        self.write : int = write
        self.move : int = move
        self.next : str = next

class TuringState:
    # A Turing state
    def __init__(self, name : str, turingSets : List[TuringSet]) -> None:
        self.name : str = name
        self.turingSets : List[TuringSet] = turingSets

def parseLines(lines : List[str]) -> Dict[str, TuringState]:
    turingStates : Dict[str, TuringState] = {}
    for i in range(3, len(lines), 10):
        turingSets : List [TuringSet]= []
        turingSets.append(TuringSet(int(lines[i+2][22]), 1 if lines[i+3][27] == "r" else -1, lines[i+4][26]))
        turingSets.append(TuringSet(int(lines[i+6][22]), 1 if lines[i+7][27] == "r" else -1, lines[i+8][26]))
        turingStates[lines[i][9]] = TuringState(lines[i][9], turingSets)
    return turingStates

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    turingStates : Dict[str, TuringState] = parseLines(lines)
    turingTape : List[int] = [0]
    turingHead : int = 0
    turingState : str = "A"
    stepTarget : int = int(lines[1].split(" ")[5])
    stepCount : int = 0
    while stepCount < stepTarget:
        stepCount += 1
        currentSpot : int = turingTape[turingHead]
        turingTape[turingHead] = turingStates[turingState].turingSets[currentSpot].write
        turingHead += turingStates[turingState].turingSets[currentSpot].move
        turingState = turingStates[turingState].turingSets[currentSpot].next

        if turingHead < 0:
            turingTape.insert(0, 0)
            turingHead = 0
        elif turingHead >= len(turingTape):
            turingTape.append(0)

    return f"The number of ones in the turing tape checkSum is {turingTape.count(1)}."

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
    print("Advent of Code 2017 Day " + AOCDAY + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))

main()