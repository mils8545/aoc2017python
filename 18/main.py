import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "18"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Instruction:
    def __init__(self, instruction: str, register: str, value: str) -> None:
        self.instruction : str = instruction
        self.register : str = register
        self.value : str = value
    def __str__(self) -> str:
        return f"{self.instruction} {self.register} {self.value}"

class ProgramState:
    def __init__(self, instructions: List[Instruction], programID: int) -> None:
        self.instructions : List[Instruction] = instructions
        self.programID : int = programID
        self.registers : dict[str, int] = {}
        self.progCounter : int = 0
        self.waiting : bool = False
        for instruction in instructions:
            self.registers[instruction.register] = 0
        self.registers["p"] = programID
        self.registers["1"] = 1

    def run(self, inputs: List[int]) -> List[int]:
        self.waiting = False
        outputs : List[int] = []
        while self.progCounter < len(self.instructions):
            instruction : Instruction = self.instructions[self.progCounter]
            numeric : bool = instruction.value.replace("-","").isnumeric()
            intValue : int = 0
            if numeric:
                intValue = int(instruction.value)
            else:
                intValue = self.registers[instruction.value]
            if instruction.instruction == "snd":
                outputs.append(intValue)
            elif instruction.instruction == "set":
                self.registers[instruction.register] = intValue
            elif instruction.instruction == "add":
                self.registers[instruction.register] += intValue
            elif instruction.instruction == "mul":
                self.registers[instruction.register] *= intValue
            elif instruction.instruction == "mod":
                self.registers[instruction.register] %= intValue
            elif instruction.instruction == "rcv":
                if len(inputs) == 0:
                    self.waiting = True
                    return outputs
                self.registers[instruction.register] = inputs.pop(0)
            elif instruction.instruction == "jgz":
                if self.registers[instruction.register] > 0:
                    self.progCounter += intValue - 1
            self.progCounter += 1
        return outputs

def part1(lines : List[str]) -> str:
    instructions : List[Instruction] = []
    for line in lines:
        splitLine : List[str] = line.split()
        instructions.append(Instruction(splitLine[0], splitLine[1], splitLine[-1]))
    registers : dict[str, int] = {}
    for instruction in instructions:
        registers[instruction.register] = 0
    progCounter : int = 0
    lastSound : int = 0

    while progCounter < len(instructions):
        instruction : Instruction = instructions[progCounter]
        numeric : bool = instruction.value.replace("-","").isnumeric()
        intValue : int = 0
        if numeric:
            intValue = int(instruction.value)
        else:
            intValue = registers[instruction.value]

        if instruction.instruction == "snd":
            lastSound = registers[instruction.register]
        elif instruction.instruction == "set":
            registers[instruction.register] = intValue
        elif instruction.instruction == "add":
            registers[instruction.register] += intValue
        elif instruction.instruction == "mul":
            registers[instruction.register] *= intValue
        elif instruction.instruction == "mod":
            registers[instruction.register] %= intValue
        elif instruction.instruction == "rcv":
            if registers[instruction.register] != 0:
                return f"The last sound played was {lastSound}."
        elif instruction.instruction == "jgz":
            if registers[instruction.register] > 0:
                progCounter += intValue - 1
        progCounter += 1

    return f"Not Implemented"

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    instructions : List[Instruction] = []
    for line in lines:
        splitLine : List[str] = line.split()
        instructions.append(Instruction(splitLine[0], splitLine[1], splitLine[-1]))
    program0 : ProgramState = ProgramState(instructions, 0)
    program1 : ProgramState = ProgramState(instructions, 1)
    prog1Count : int = 0
    program0sends : List[int] = []
    program1sends : List[int] = []

    while True:
        program0sends = program0.run(program1sends).copy()
        program1sends = program1.run(program0sends).copy()
        prog1Count += len(program1sends)
        if len(program0sends) == 0 and len(program1sends) == 0:
            return f"Program 1 sends a total of {prog1Count} times."

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