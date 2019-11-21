import random

class Ability:

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        rand_hit = random.randint(0,self.attack_strength)
        return rand_hit

        ''' Return a value between 0 and the value set by self.max_damage.'''

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        # ''' Return a random value between 0 and the initialized max_block strength. '''
        # return random.randint(0,max_block)
     pass
# class Hero:
#     def __init__(self, name, starting_health=100):
#         self.name = name
#         self.starting_health = starting_health
#         self.current_health = starting_health
#         self.abilities = []
#         self.armors = []
# #     self.deaths = 0
# #         # self.kills = 0
# #
#     def add_ability(self, ability):
#         ''' Add ability to abilities list '''
#         self.abilities.append(ability)

#     def attack(self):
#         '''Calculate the total damage from all ability attacks.
#         return: total:Int'''
#         total_damage = 0
#         for ability in self.abilities:
#             total_damage += ability.attack()
#         return total_damage

#     def add_armor(self, armor):
#         self.armors.append(armor)

#     def defend(self):
#         total_block = 0
#         for armor in self.armors:
#             total_block += armor.block()
#         return total_block

      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.

#
#     def defend(self, incoming_damage):
#
#     def take_damage(self, damage):
#
#     def is_alive(self):
#
#     def fight(self, opponent):

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
 