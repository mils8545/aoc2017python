import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "23"

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
        for letter in "abcdefgh":
            self.registers[letter] = 0

    def run(self, regA : int = 0, debugPrint : bool = False) -> int:
        self.waiting = False
        mulCount : int = 0
        self.registers['a'] = regA
        outputs : List[int] = []
        while self.progCounter < len(self.instructions):
            instruction : Instruction = self.instructions[self.progCounter]
            if debugPrint:
                print(self.registers)
                print(self.progCounter, instruction.instruction, instruction.register, instruction.value)
            numeric : bool = instruction.value.replace("-","").isnumeric()
            intValue : int = 0
            if str(instruction.register) not in self.registers:
                self.registers[instruction.register] = int(instruction.register)
            if numeric:
                intValue = int(instruction.value)
            else:
                intValue = self.registers[instruction.value]
            if instruction.instruction == "set":
                self.registers[instruction.register] = intValue
            elif instruction.instruction == "sub":
                self.registers[instruction.register] -= intValue
            elif instruction.instruction == "mul":
                self.registers[instruction.register] *= intValue
                mulCount += 1
            elif instruction.instruction == "jnz":
                regNumeric : bool = instruction.register.replace("-","").isnumeric()
                regValue : int = 0
                if regNumeric:
                    regValue = int(instruction.register)
                else:
                    regValue = self.registers[instruction.register]
                if self.registers[instruction.register] != 0:
                    self.progCounter += intValue - 1
            self.progCounter += 1
        return mulCount

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    instructions : List[Instruction] = []
    for line in lines:
        instruction : Instruction = Instruction(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2])
        instructions.append(instruction)
    programState : ProgramState = ProgramState(instructions, 0)
    mulCount : int = programState.run()

    return f"The program runs mul {mulCount} times."

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    instructions : List[Instruction] = []
    for line in lines:
        instruction : Instruction = Instruction(line.split(" ")[0], line.split(" ")[1], line.split(" ")[2])
        instructions.append(instruction)

    b : int = int(instructions[0].value) * int(instructions[4].value) - int(instructions[5].value)
    c : int = b - int(instructions[7].value)

    primes : List[int] = [2, 3]

    for i in range(5, c+1, 2):
        isPrime : bool = True
        for prime in primes:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    primeCount : int = 0
    for i in range(b, c+1, 17):
        if i not in primes:
            primeCount += 1

    print(b, c, primeCount)
    return f"Register h is {primeCount} which is the number of primes between {b} and {c}."

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