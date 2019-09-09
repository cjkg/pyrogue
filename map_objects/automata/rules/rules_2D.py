"""
Totalistic rules for 2D cellular automata.
"""

def cave_four_five(state, neighbors):
    """
    basic idea for the five rule taken from here:
    http://roguebasin.roguelikedevelopment.org/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels#Rule_Tweaking
    it essentially makes cells more like their neighbors over time
    """
    neighbor_sum = sum(neighbors)
    if state == 1 and neighbor_sum >= 4:
        return 1
    elif state == 0 and neighbor_sum >= 5:
        return 1
    else:
        return 0
    
def cave_orphan_handler(state, neighbors):
    """
    basic idea for the orphan handler taken from here:
    http://roguebasin.roguelikedevelopment.org/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels#Rule_Tweaking
    essentially, it takes small clusters of on and turns them to off, and small
    clusters of off and turns them to on. This removes isolated pockets of the
    various values from cluttering up the map.
    """
    
    neighbor_sum = sum(neighbors)
    if state == 1 and neighbor_sum <= 2:
        return 0
    elif state == 0 and neighbor_sum >=7:
        return 1
    else:
        return state
    
def cave_rounder(state, neighbors):
    """If exactly two adjacent sides are filled in, and the remainder off,
    return 1 to round out the corner to make it more cavelike"""
    if (neighbors == [1, 1, 1, 1, 0, 0, 0, 1] or 
        neighbors == [1, 1, 0, 0, 0, 1, 1, 1] or 
        neighbors == [0, 1, 1, 1, 1, 1, 0, 0] or 
        neighbors == [0, 0, 0, 1, 1, 1, 1, 1] ):
        return 1
    else:
        return state
