import numpy as np

def find_neighbors(state, x_coord, y_coord):
    """
    find "Von Neumann" neighbors' (N, W, S, E) values and return their coords
    if their value is in the condition set
    """
    neighbors = []
    
    cardinal_dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    for direction in cardinal_dirs:
        try:
            neighbors.append((x_coord + direction[0], y_coord + direction[1]))
        except IndexError:
            pass

    return neighbors


def find_neighbors_cond(state, x_coord, y_coord, condition):
    """
    find "Von Neumann" neighbors' (N, W, S, E) values and return their coords
    if their value is in the condition set
    """
    neighbors = []
    
    cardinal_dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    for direction in cardinal_dirs:
        try:
            if state[y_coord + direction[1]][x_coord + direction[0]] in condition:
                neighbors.append((x_coord + direction[0], y_coord + direction[1]))
        except IndexError:
            pass

    return neighbors

def euclid_distance(x_1, y_1, x_2, y_2):
    return ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5
    

def manhattan_distance(x_1, y_1, x_2, y_2):
    return np.absolute(x_1 + x_2) + np.absolute(y_1 + y_2)
    

def get_slope(point_1, point_2):
    """get the slope of a line"""
    if point_1 == point_2:
        return np.NINF #always want the start_point to be first
    elif point_1[0] == point_2[0]:
        return np.inf #if slope undefined, it will always be last point in map
    else:
        return (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
    
def print_output(state):
    """
    turns 1's into '#', turns 0's into negative space (i.e., spaces)
    spaces, as it makes it easier to see on the terminal than an ndarray
    of 1's and 0's while debugging.
    """
    print_map = []
    
    for array in state:
        print_string = ''
        for j in array:
            if j == 1:
                print_string += '#'
            else:
                print_string += ' '
        print_map += print_string
        print(print_string)
        