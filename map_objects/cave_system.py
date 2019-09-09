from automata.automatonTwoDim import TwoDimAutomaton as Automaton
from map_utils import euclid_distance, find_neighbors_cond, find_neighbors, print_output
import numpy as np

class CaveSystem:
    def __init__(self, width, height, floors, min_room_size=12,
                 init_wall_chance=0.25):
        self.width = width
        self.height = height
        self.floors = floors
        self.min_room_size = min_room_size
        self.init_wall_chance = init_wall_chance

    def build_floors(self):
        floors = []
        for floor in range(self.floors):
            floor_state = self.create_floor()

            floors.append(floor_state)
        return floors

    def cave_finder(self, cave_state, max_tries=500):
        caves = []
        done = set()

        for i in range(max_tries):

            for x in range(self.width):
                for y in range(self.height):
                    if cave_state[y][x] == 0 and (x, y) not in done:
                        start_point = (x, y)
                        break
                else:
                    continue
                break
            else:
                return caves

            stack = [start_point]
            cave = set(stack)
            while stack != []:
                curr_point = stack.pop()
                curr_neighbors = find_neighbors_cond(cave_state, curr_point[0],
                                                     curr_point[1], {0})

                for neighbor in curr_neighbors:
                    if neighbor not in done:
                        cave.add(neighbor)
                        done.add(neighbor)
                        stack.append(neighbor)

            caves.append(cave)


        caves = []

        return caves

    def create_floor(self, max_tries=500):
        start_state = np.zeros((self.height, self.width), int)

        for y in range(self.height):
            for x in range(self.width):
                if np.random.random() < self.init_wall_chance:
                    start_state[y][x] = 1

        cave_digger = Automaton('cave_four_five')


        cave_state = cave_digger.automate_cells(start_state, 5)
        

        cave_floor = self.cave_checker(cave_state)
        return cave_floor

    def cave_connector(self, cave_one_set, cave_two_set, curr_state):
        
        cave_1_index = np.random.randint(len(cave_one_set)-1)
        cave_2_index = np.random.randint(len(cave_two_set)-1)
        point_1 = list(cave_one_set)[cave_1_index]
        point_2 = list(cave_two_set)[cave_2_index]
        
        point_1_x = int(point_1[0])
        point_1_y = int(point_1[1])
        
        point_2_x = int(point_2[0])
        point_2_y = int(point_2[1])
        
        while (point_1_x, point_1_y) not in cave_two_set:
            start_dist = euclid_distance(point_1_x, point_1_y, point_2_x, point_2_y)
            neighbors = find_neighbors(curr_state, point_1_x, point_1_y)
            neighbors_shuffled = sorted(neighbors, key=lambda k: np.random.random())
            for neighbor in neighbors_shuffled:
                neighbor_dist = euclid_distance(neighbor[0], neighbor[1], point_2_x, point_2_y)
                if neighbor_dist < start_dist:
                    point_1_x = int(neighbor[0])
                    point_1_y = int(neighbor[1])
                    curr_state[point_1_y][point_1_x] = 0 
                    break
               
        return curr_state

    def cave_checker(self, state):
        caves = self.cave_finder(state)

        for cave in caves:
            if len(cave) < self.min_room_size:
                for cell in cave:
                    state[cell[1]][cell[0]] = 1
            

        caves = self.cave_finder(state)
        caves.sort(key=len, reverse=True)
        while len(caves) > 1:
            caves = self.cave_connector(caves[0], caves[1], state)
            caves = self.cave_finder(state)
        
        cleaner = Automaton('cave_orphan_handler')
        rounder = Automaton('cave_rounder')
        clean_state = cleaner.automate_cells(state, 1)
        rounded_state = rounder.automate_cells(clean_state, 1)

        return rounded_state
