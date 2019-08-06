from random_utils import roll_dice
import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, strength=1, agility=1, intelligence=1,
                 charisma=1, perception=1, endurance=1,
                 attack_die={"dice_count":1,"die_faces":20, "die_bonus":0}, xp=0):
        self.base_max_hp = hp
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma
        self.perception = perception
        self.endurance = endurance
        self.base_defense = defense
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

    @property
    def main_hand_damage_bonus(self):
        bonus = 0
        
        if self.owner and self.owner.equipment:
            bonus += self.owner.equipment.main_hand_weapon_damage_bonus
        
        if self.owner and self.owner.equipment and self.owner.equipment.main_hand_weapon_type == 'melee':
            bonus += self.str_mod

        if self.owner and self.owner.equipment and self.owner.equipment.main_hand_weapon_type == 'ranged':
            bonus += self.agi_mod

        return bonus
    
    @property
    def main_hand_damage_msg(self):
        if self.owner and self.owner.equipment and self.owner.equipment.main_hand:
            return '{0}d{1}+{2} {3} dmg'.format(self.owner.equipment.main_hand.equippable.damage_dice_count,
                              self.owner.equipment.main_hand.equippable.damage_die_face,
                              self.main_hand_damage_bonus,
                              self.owner.equipment.main_hand_weapon_type)
        else:
            return '{0} unarmed dmg'.format(max({1, (1 + self.str_mod)}))
            
    
    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus + self.agi_mod

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
        if base_score == 1:
            return -3
        elif base_score == 2:
            return -2
        elif base_score == 3:
            return -1
        elif base_score in {4, 5, 6}:
            return 0
        elif base_score == 7:
            return 1
        elif base_score == 8:
            return 2
        elif base_score == 9:
            return 3
        elif base_score == 10:
            return 4
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
            results.append({'message': Message('{0} fumbles the strike on {1}!'.format(
                self.owner.name.capitalize(), target.name), libtcod.yellow)})
                #Need to have a critical miss
        elif attack_roll == 20:
            if self.owner and self.owner.equipment and self.owner.equipment.main_hand:
                damage = 2 * max({1, (self.owner.equipment.main_hand.equippable.damage_dice_count *
                              self.owner.equipment.main_hand.equippable.damage_die_face + 
                              self.main_hand_damage_bonus)})
            else:
                damage = 2 * max({1, (1 + self.str_mod)}) #unarmed strike, max needed to ensure always do at least one pt of dmg
                
            results.append({'message': Message('{0} critically hits {1}! ({2})'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.red)})
            results.extend(target.fighter.take_damage(damage))
        elif attack_roll + self.attack_die['die_bonus'] >= target.fighter.defense:
            if self.owner and self.owner.equipment and self.owner.equipment.main_hand:
                damage = max({1, (roll_dice(self.owner.equipment.main_hand.equippable.damage_dice_count, self.owner.equipment.main_hand.equippable.damage_die_face) + self.main_hand_damage_bonus)})
            else:
                damage = max({1, (1 + self.str_mod)}) #unarmed strike, max needed to ensure always do at least one pt of dmg
            
            results.append({'message': Message('{0} hits {1}! ({2})'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.red)})
            results.extend(target.fighter.take_damage(damage))
        else:
            damage = 0
            results.append({'message': Message('{0} misses {1}!'.format(
                self.owner.name.capitalize(), target.name), libtcod.yellow)})

        return results
