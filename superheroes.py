import random

class Ability:

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        rand_hit = random.randint(0,self.max_damage)
        return rand_hit

        ''' Return a value between 0 and the value set by self.max_damage.'''

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        rand_block = random.randint(0, self.max_block)
        return rand_block
    
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health   
        
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.


    def take_damage(self, damage):
        defense = self.defend(damage)
        self.current_health -= damage - defense
#
#     def is_alive(self):
#
#     def fight(self, opponent):

if __name__ == "__main__":
        hero = Hero("Grace Hopper", 200)
        shield = Armor("Shield", 75)
        hero.add_armor(shield)
        hero.take_damage(50)
        print(hero.current_health)