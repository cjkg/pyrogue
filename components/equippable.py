class Equippable:
    def __init__(self, slot, damage_dice_count=None, damage_die_face=None,
                 damage_bonus=0, weapon_type=None, damage_type=None, 
                 ammo_type=None, reach=None, attack_die_bonus=0, 
                 defense_bonus=0, max_hp_bonus=0, str_bonus=0, agi_bonus=0, 
                 int_bonus=0, will_bonus=0, cha_bonus=0, per_bonus=0, 
                 end_bonus=0):
        self.slot = slot
        self.damage_dice_count = damage_dice_count
        self.damage_die_face = damage_die_face
        self.damage_bonus = damage_bonus
        self.weapon_type = weapon_type
        self.damage_type = damage_type
        self.ammo_type = ammo_type
        self.reach = reach
        self.attack_die_bonus = attack_die_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.str_bonus = str_bonus
        self.agi_bonus = agi_bonus
        self.int_bonus = int_bonus
        self.will_bonus = will_bonus
        self.cha_bonus = cha_bonus
        self.per_bonus = per_bonus
        self.end_bonus = end_bonus
