import easygui
import time
from typing import List
from typing import Union

AOCDAY: str = "20"

def readFile(fileName : str) -> List[str]: 
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines : list[str] = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

class Particle:
    def __init__(self, x: int, y: int, z: int, vx: int, vy: int, vz: int, ax: int, ay: int, az: int) -> None:
        self.x : int = x
        self.y : int = y
        self.z : int = z
        self.vx : int = vx
        self.vy : int = vy
        self.vz : int = vz
        self.ax : int = ax
        self.ay : int = ay
        self.az : int = az
    def __str__(self) -> str:
        return f"p=({self.x},{self.y},{self.z}), v=({self.vx},{self.vy},{self.vz}), a=({self.ax},{self.ay},{self.az})"
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    def run(self) -> None:
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
    def manhattanDistance(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)
    def manhattanVelocity(self) -> int:
        return abs(self.vx) + abs(self.vy) + abs(self.vz)
    def manhattanAcceleration(self) -> int:
        return abs(self.ax) + abs(self.ay) + abs(self.az)

def partLines(lines : List[str]) -> List[Particle]:
    particles : List[Particle] = []
    for line in lines:
        line = line.replace("p=<", "")
        line = line.replace("v=<", "")
        line = line.replace("a=<", "")
        line = line.replace(">", "")
        line = line.replace(" ", "")
        line = line.split(",")
        particles.append(Particle(int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8])))
    return particles

def part1(lines : List[str]) -> str:
    # Code the solution to part 1 here, returning the answer as a string
    particles : List[Particle] = partLines(lines)
    minAcceleration : int = particles[0].manhattanAcceleration()
    minAccelerationIndex : int = 0
    for i, particle in enumerate(particles):
        if particle.manhattanAcceleration() < minAcceleration:
            minAcceleration = particle.manhattanAcceleration()
            minAccelerationIndex = i
    return f"The particle with the lowest acceleration is {minAccelerationIndex}"

def part2(lines : List[str]) -> str:
    # Code the solution to part 2 here, returning the answer as a string
    particles : List[Particle] = partLines(lines)
    for i in range(50):
        for particle in particles:
            particle.run()
        collisionIndexes : List[int] = []
        for j in range(len(particles)-1):
            for k in range(j+1, len(particles)):
                if particles[j] == particles[k]:
                    collisionIndexes.append(j)
                    collisionIndexes.append(k)
        collisionIndexes = list(set(collisionIndexes))
        collisionIndexes.sort(reverse=True)
        for index in collisionIndexes:
            del particles[index]
        print (f"Particles left: {len(particles)}")
    return f"There are {len(particles)} particles left after collisions."

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