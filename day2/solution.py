import numpy as np
import pandas as pd

data = pd.read_csv('input.txt', sep=",", header=None)

intcode = data.to_numpy()[0]

index = 0

def loop(index, intcode):
    if load_values(index, intcode):
        index += 4
        loop(index, intcode)

def load_values(index, intcode):
    opcode = intcode[index]

    if opcode != 1 and opcode != 2 and opcode != 99:
        print("ERROR opcode {0} not recognized".format(opcode))
        return False

    if opcode == 99:
        print("Finished program. Position 0 = {0}".format(intcode[0]))
        return False

    pos1 = intcode[index + 1]
    pos2 = intcode[index + 2]
    ret = intcode[index + 3]

    print("op={0}, pos1={1}, pos2={2}, ret={3}".format(opcode, pos1, pos2, ret))

    val1 = intcode[pos1]
    val2 = intcode[pos2]

    new_value = 0

    if opcode == 1: # Add
        new_value = val1 + val2

    if opcode == 2: # Multiply
        new_value = val1 * val2

    intcode[ret] = new_value

    return True

loop(index, intcode)