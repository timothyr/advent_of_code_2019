import numpy as np
import pandas as pd

data = pd.read_csv('input.txt', sep=",", header=None)

intcode = data.to_numpy()[0]
intcode_modified_bool = np.zeros((1, intcode.shape[0]))[0]

intcode_modified_bool[1] = 1
intcode_modified_bool[2] = 1

index = 0

def loop(index, intcode):
    if load_values(index, intcode):
        index += 4
        loop(index, intcode)

def get_value(index, intcode):
    val = intcode[index]
    modified = bool(intcode_modified_bool[val])
    return val, modified

def load_values(index, intcode):
    opcode = intcode[index]

    if opcode != 1 and opcode != 2 and opcode != 99:
        print("ERROR opcode {0} not recognized".format(opcode))
        return False

    if opcode == 99:
        print("Finished program. Position 0 = {0}".format(intcode[0]))
        return False

    pos1, mod1 = get_value(index + 1, intcode)
    pos2, mod2 = get_value(index + 2, intcode)
    ret = intcode[index + 3]

    intcode_modified_bool[index + 3] = 1

    print("op={0}, pos1={1}, pos2={2}, ret={3}".format(opcode, pos1, pos2, ret))

    val1 = intcode[pos1]
    val2 = intcode[pos2]

    new_value = 0

    if opcode == 1: # Add
        new_value = val1 + val2

    if opcode == 2: # Multiply
        new_value = val1 * val2

    if mod1 or mod2:
        intcode_modified_bool[ret] = 1

    intcode[ret] = new_value

    print("i[{0}] = {1}: ({2} {3} {4})".format(
        ret, 
        (new_value, '?')[mod1 or mod2],
        (val1, '?')[mod1],
        ('+', '*')[bool(opcode - 1)],
        (val2, '?')[mod2]))

    return True

loop(index, intcode)