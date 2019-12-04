import numpy as np
import pandas as pd

data = pd.read_csv('input.txt', sep="\n", header=None)

print(data)

def compute_max_matrix_size(coords_arr):
    x_pos = 0
    y_pos = 0

    max_x = 0
    max_y = 0

    min_x = 0
    min_y = 0

    coords = coords_arr.split(',')

    for coord in coords:
        direction = coord[0]
        distance = int(coord[1:])

        if direction == 'R':
            x_pos += distance
        if direction == 'L':
            x_pos -= distance
        if direction == 'U':
            y_pos += distance
        if direction == 'D':
            y_pos -= distance

        if x_pos > max_x:
            max_x = x_pos
        if x_pos < min_x:
            min_x = x_pos
        if y_pos > max_y:
            max_y = y_pos
        if y_pos < min_y:
            min_y = y_pos

    return min_x, min_y, max_x, max_y


# Compare matrix 1 and 2 and take largest x,y size of both
def get_matrix_size(data):
    min_x1, min_y1, max_x1, max_y1 = compute_max_matrix_size(data[0][0])
    min_x2, min_y2, max_x2, max_y2 = compute_max_matrix_size(data[0][1])

    min_x = min(min_x1, min_x2)
    min_y = min(min_y1, min_y2)
    max_x = max(max_x1, max_x2)
    max_y = max(max_y1, max_y2)

    x = abs(min_x) + max_x + 1 # off by 1 lol
    y = abs(min_y) + max_y + 1
    center_x = abs(min_x)
    center_y = abs(min_y)

    print("min_x {0} : {1}".format(min_x1, min_x2))
    print("max_x {0} : {1}".format(max_x1, max_x2))
    print("min_y {0} : {1}".format(min_y1, min_y2))
    print("max_y {0} : {1}".format(max_y1, max_y2))

    print("map size = ({0}, {1}) and center = ({2}, {3})".format(x,y, center_x,center_y))

    return x, y, center_x, center_y

# Create numpy boolean matrix with shape (x,y) and filled with False
def create_numpy_matrix(x, y):
    return np.full((x,y), False, dtype=bool)

def fill_matrix(matrix, coords_arr, center_x, center_y):
    x = center_x
    y = center_y

    coords = coords_arr.split(',')

    for coord in coords:
        direction = coord[0]
        distance = int(coord[1:])

        if direction == 'R':
            matrix[x:x+distance, y] = True
            x = x + distance
        if direction == 'L':
            matrix[x-distance:x, y] = True
            x = x - distance
        if direction == 'U':
            matrix[x, y:y+distance] = True
            y = y + distance
        if direction == 'D':
            matrix[x, y-distance:y] = True
            y = y - distance

# Use Manhatten distance to find closest intersection
# Manhatten distance = abs(x1 - x2) + abs(y1 - y2)
def find_closest_intersection(intersections, center_x, center_y):
    closest_distance = np.Infinity
    closest_x = np.Infinity
    closest_y = np.Infinity

    for i in intersections:
        x = i[0]
        y = i[1]

        if x == center_x and y == center_y:
            continue

        distance_x = abs(center_x - x)
        distance_y = abs(center_y - y)

        distance = distance_x + distance_y
        if distance < closest_distance:
            closest_distance = distance
            closest_x = distance_x
            closest_y = distance_y

    return closest_distance, closest_x, closest_y

def main():        
    x, y, center_x, center_y = get_matrix_size(data)
    matrix1 = create_numpy_matrix(x, y)
    matrix2 = create_numpy_matrix(x, y)

    fill_matrix(matrix1, data[0][0], center_x, center_y)
    print("matrix1 distance = {0}".format(np.count_nonzero(matrix1)))

    fill_matrix(matrix2, data[0][1], center_x, center_y)
    print("matrix2 distance = {0}".format(np.count_nonzero(matrix2)))

    intersections = matrix1 & matrix2
    print("number of intersections = {0}".format(np.count_nonzero(intersections)))

    intersections = np.transpose(np.nonzero(intersections)) # convert into array of x,y tuples

    closest_distance, closest_x, closest_y = find_closest_intersection(intersections, center_x, center_y)

    print("------------------------------------------------------")
    print("Solution 1: Closest distance = {0} @ (x:{1}, y:{2})".format(closest_distance, closest_x, closest_y))
    print("------------------------------------------------------")

main()