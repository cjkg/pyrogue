from random import randint

def from_dungeon_level(table, dungeon_level):
    for (value, level) in reversed(table):
        if dungeon_level >= level:
            return value

    return 0

def random_choice_index(chances):
    random_chance = randint(1, sum(chances))

    running_sum = 0
    choice = 0
    for w in chances:
        running_sum += w

        if random_chance <= running_sum:
            return choice
        choice += 1

def random_choice_from_dict(choice_dict):
    choices = list(choice_dict.keys())
    chances = list(choice_dict.values())

    return choices[random_choice_index(chances)]

def roll_die(die_sides):
    if die_sides == 0:
        return 0

    return randint(1, die_sides)

def roll_dice(dice_count, side_count):
    if side_count == 0:
        return 0
    
    roll = 0
    for die in range(0, dice_count):
        roll += roll_die(side_count)
        
    return roll