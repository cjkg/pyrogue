from random_utils import roll_dice
import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, strength, agility, intelligence,
                 will, charisma, perception, endurance,
                 attack_die={"dice_count":1,"die_faces":20, "die_bonus":0}, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.will = will
        self.charisma = charisma
        self.perception = perception
        self.endurance = endurance
        self.base_defense = defense
        self.base_power = power
        self.base_attack_die = attack_die
        self.xp = xp

    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def attack_die(self):
        bonus = 0
        attack_die_update = self.base_attack_die

        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.attack_die_bonus
        
        if self.owner and self.owner.equipment and self.owner.equipment.main_hand_weapon_type == 'melee':
            bonus += self.str_mod
        
        if self.owner and self.owner.equipment and self.owner.equipment.main_hand_weapon_type == 'ranged':
            bonus += self.agi_mod
        
        attack_die_update["die_bonus"] = bonus
        return attack_die_update
    """
    @property
    def damage_die(self):

        if self.owner and self.owner.equipment:
            damage_die

        bonus = 0

        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.damage_die_bonus

        self.base_damage_die["bonus"] += bonus
    """
    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    @property
    def str_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.str_bonus

        return self.find_mod(self.strength + bonus)

    @property
    def agi_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.agi_bonus
        
        return self.find_mod(self.agility + bonus)
    
    @property
    def int_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.int_bonus
        
        return self.find_mod(self.intelligence + bonus)

    @property
    def will_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.will_bonus
        
        return self.find_mod(self.will + bonus)

    @property
    def cha_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.cha_bonus
        
        return self.find_mod(self.charisma + bonus)
    
    @property
    def per_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.per_bonus
        
        return self.find_mod(self.perception + bonus)

    @property
    def end_mod(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.end_bonus
        
        return self.find_mod(self.endurance + bonus)

    def find_mod(self, base_score):
        if base_score <= 3:
            return -4
        elif base_score == 4:
            return -3
        elif base_score in {5, 6}:
            return -2
        elif base_score in {7, 8}:
            return -1
        elif base_score in set(range(9, 13)):
            return 0
        elif base_score in {13, 14}:
            return 1
        elif base_score in {15, 16}:
            return 2
        elif base_score == 17:
            return 3
        elif base_score == 18:
            return 4
        elif base_score in {19, 20}:
            return 5
        elif base_score == 21:
            return 6
        elif base_score == 22:
            return 7
        elif base_score == 23:
            return 8
        elif base_score == 24:
            return 9
        elif base_score >= 25:
            return 10
        else:
            return 0


    def take_damage(self, amount):
        results = []
        self.hp -= amount

        if self.hp <= 0:
            self.hp = 0
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []

        attack_roll = roll_dice(self.attack_die['dice_count'], self.attack_die['die_faces'])
        if attack_roll == 1:
            damage = 0
            results.append({'message': Message('{0} attacks {1} and critically misses! {2}'.format(
                self.owner.name.capitalize(), target.name, attack_roll), libtcod.yellow)})
                #Need to have a critical miss
        elif attack_roll == 20:
            damage = self.power * 2
            results.append({'message': Message('{0} crits {1} for {2} damage! {3}'.format(
                self.owner.name.capitalize(), target.name, str(damage), attack_roll), libtcod.red)})
            results.extend(target.fighter.take_damage(damage))
        elif attack_roll + self.attack_die['die_bonus'] >= target.fighter.defense:
            damage = self.power
            results.append({'message': Message('{0} attacks {1} for {2} damage! {3}'.format(
                self.owner.name.capitalize(), target.name, str(damage), attack_roll), libtcod.red)})
            results.extend(target.fighter.take_damage(damage))
        else:
            damage = 0
            results.append({'message': Message('{0} attacks {1} and misses! {2}'.format(
                self.owner.name.capitalize(), target.name, attack_roll), libtcod.yellow)})

        return results
