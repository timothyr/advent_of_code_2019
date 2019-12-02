import numpy as np
import pandas as pd

data = pd.read_csv('input.txt', sep="\n", header=None)

# Part 1

def calculate_fuel_required(mass):
    return int(mass / 3) - 2 # divide by 3, round down, subtract 2

fuel = data.apply(calculate_fuel_required, axis=1)
fuel_required_sum = fuel.values.sum()

print("Fuel required = {0}".format(fuel_required_sum))

# Part 2

def calculate_fuel_recursive(mass):
    fuel_required = calculate_fuel_required(mass)
    if fuel_required > 0:
        return fuel_required + calculate_fuel_recursive(fuel_required)
    return 0

recursive_fuel = data.apply(calculate_fuel_recursive, axis=1)
recursive_fuel_sum = recursive_fuel.values.sum()

print("Fuel required (recursive) = {0}".format(recursive_fuel_sum))