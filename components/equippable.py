class Equippable:
    def __init__(self, slot, dmg_die=None, weapon_type=None, damage_type=None, 
                 attack_die_bonus=0, power_bonus=0, 
                 defense_bonus=0, max_hp_bonus=0, str_bonus=0, agi_bonus=0, 
                 int_bonus=0, will_bonus=0, cha_bonus=0, per_bonus=0, end_bonus=0):
        self.slot = slot
        self.dmg_die = dmg_die
        self.weapon_type = weapon_type
        self.damage_type = damage_type
        self.attack_die_bonus = attack_die_bonus
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.str_bonus = str_bonus
        self.agi_bonus = agi_bonus
        self.int_bonus = int_bonus
        self.will_bonus = will_bonus
        self.cha_bonus = cha_bonus
        self.per_bonus = per_bonus
        self.end_bonus = end_bonus
