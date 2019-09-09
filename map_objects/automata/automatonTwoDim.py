"""
2D Cellular Automaton.
"""
import numpy as np
import automata.rules.rules_2D as rules_2D

class TwoDimAutomaton(object):
    def __init__(self, rule_name):
        self.rule_name = rule_name
    
    @staticmethod
    def find_neighbors(state, x_cell, y_cell, index_error_value=1):
        """
        find "Moore" neighbors around a cell. If the cell is on the edge,
        the non-existent neighbors "beyond" the edge receive a 1 value by
        default. This may seem counterintuitive, but it makes the walls of the 
        cave look much more organic. If you want to use the Von Neumann
        neighborhood for a rule, you just pick out the n, w, s, and e neighbors
        out of the list and ignore the rest.
        """
        try: #find the nw neighbor's state, set to index_error_value if none
            nw_neighbor = state[y_cell - 1][x_cell - 1]
        except IndexError:
            nw_neighbor = index_error_value
    
        try: #find the n neighbor's state, set to index_error_value if none
            n_neighbor = state[y_cell - 1][x_cell]
        except IndexError:
            n_neighbor = index_error_value
    
        try: #find the ne neighbor's state, set to index_error_value if none
            ne_neighbor = state[y_cell - 1][x_cell + 1]
        except IndexError:
            ne_neighbor = index_error_value
    
        try: #find the w neighbor's state, set to index_error_value if none
            w_neighbor = state[y_cell][x_cell - 1]
        except IndexError:
            w_neighbor = index_error_value
        
        try: #find the e neighbor's state, set to index_error_value if none
            e_neighbor = state[y_cell][x_cell + 1]
        except IndexError:
            e_neighbor = index_error_value
        
        try: #find the sw neighbor's state, set to index_error_value if none
            sw_neighbor = state[y_cell + 1][x_cell - 1]
        except IndexError:
            sw_neighbor = index_error_value
        
        try: #find the s neighbor's state, set to index_error_value if none
            s_neighbor = state[y_cell + 1][x_cell]
        except IndexError:
            s_neighbor = index_error_value
        
        try: #find the se neighbor's state, set to index_error_value if none
            se_neighbor = state[y_cell + 1][x_cell + 1]
        except IndexError:
            se_neighbor = index_error_value
       
        return [n_neighbor, ne_neighbor, e_neighbor, se_neighbor, s_neighbor, 
                sw_neighbor, w_neighbor, nw_neighbor]

    @staticmethod
    def build_walls(state, x_size, y_size):
        for i in range(0, y_size):
            for j in range(0, x_size):
                if j in {0, x_size - 1} or i in {0, y_size - 1}:
                    state[i][j] = 1
        
        return state
            
    def apply_rule(self, current_state, neighbors):
        """
        this function is one-stop shop for the automata, so that you can just
        pass the states of the cell's neighbors and get the result of the
        object's rule being applied. It returns a 1 or a 0, where 1 means the
        cell is 'on' and 0 means it is 'off.'
        """
        rule_dict = {
            'cave_four_five': rules_2D.cave_four_five,
            'cave_orphan_handler': rules_2D.cave_orphan_handler,
            'cave_rounder': rules_2D.cave_rounder
            }

        rule_function = rule_dict[self.rule_name]
        return rule_function(current_state, neighbors)

    def automate_cells(self, state, steps, make_walls = True, print_results=False):
        """
        Takes the first state you want to apply the rule to, the number of
        times you want to iterate the rule, and whether you want the states to
        be printed to the screen while it iterates. What it actually returns is
        the final state of the cells, represented in a 2D nparray of 1s and 0s,
        which are 'on' and 'off' states, respectively.
        """

        state_shape = state.shape

        last_state = state

        empty_state = np.zeros(state_shape, int)

        for step in range(0, steps):
            this_state = empty_state

            for x in range(0, state_shape[1]):
                for y in range(0, state_shape[0]):
                    this_state[y][x] = self.apply_rule(last_state[y][x], self.find_neighbors(last_state, x, y))

            if print_results:
                self.print_output(this_state)

            last_state = this_state

        if make_walls:
           last_state = self.build_walls(last_state, state_shape[1], state_shape[0])

        return last_state
