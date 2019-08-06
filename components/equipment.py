from equipment_slots import EquipmentSlots

class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, chest=None,
                 gloves=None, legs=None, feet=None, left_ring=None, 
                 right_ring=None):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.chest = chest
        self.gloves = gloves
        self.legs = legs
        self.feet = feet
        self.left_ring = left_ring
        self.right_ring = right_ring
        
    @property
    def main_hand_weapon_type(self):
        if self.main_hand and self.main_hand.equippable:
            return self.main_hand.equippable.weapon_type
    
    @property
    def main_hand_weapon_damage_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.damage_bonus
           
        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.damage_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.damage_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.damage_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.damage_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.damage_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.damage_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.damage_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.damage_bonus


        return bonus

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.max_hp_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.max_hp_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.max_hp_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_hp_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.max_hp_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.max_hp_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.defense_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.defense_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.defense_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.defense_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.defense_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.defense_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.defense_bonus

        return bonus

    @property
    def attack_die_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.attack_die_bonus
            
        if self.off_hand and self.main_hand.equippable:
            bonus += self.off_hand.equippable.attack_die_bonus
            
        if self.head and self.head.equippable:
            bonus += self.head.equippable.attack_die_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.attack_die_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.attack_die_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.attack_die_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.attack_die_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.attack_die_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.attack_die_bonus

        return bonus

    @property
    def damage_bonus(self):
        bonus = 0

        if self.head and self.head.equippable:
            bonus += self.head.equippable.damage_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.damage_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.damage_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.damage_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.damage_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.damage_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.damage_bonus
        

        return bonus

    @property
    def str_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.str_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.str_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.str_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.str_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.str_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.str_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.str_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.str_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.str_bonus

        return bonus

    @property
    def agi_bonus(self):
        bonus = 0
    
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.agi_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.agi_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.agi_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.agi_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.agi_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.agi_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.agi_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.agi_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.agi_bonus

        return bonus

    @property
    def int_bonus(self):
        bonus = 0
        
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.int_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.int_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.int_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.int_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.int_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.int_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.int_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.int_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.int_bonus

        return bonus

    @property
    def cha_bonus(self):
        bonus = 0
    
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.cha_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.cha_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.cha_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.cha_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.cha_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.cha_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.cha_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.cha_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.cha_bonus

        return bonus

    @property
    def per_bonus(self):
        bonus = 0
    
        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.per_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.per_bonus
        
        if self.head and self.head.equippable:
            bonus += self.head.equippable.per_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.per_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.per_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.per_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.per_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.per_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.per_bonus
        
        return bonus
        
    @property
    def end_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.end_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.end_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.end_bonus
        
        if self.chest and self.chest.equippable:
            bonus += self.chest.equippable.end_bonus
            
        if self.gloves and self.gloves.equippable:
            bonus += self.gloves.equippable.end_bonus
        
        if self.legs and self.legs.equippable:
            bonus += self.legs.equippable.end_bonus
            
        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.end_bonus
            
        if self.left_ring and self.left_ring.equippable:
            bonus += self.left_ring.equippable.end_bonus
            
        if self.right_ring and self.right_ring.equippable:
            bonus += self.right_ring.equippable.end_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results