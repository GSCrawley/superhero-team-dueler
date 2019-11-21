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
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0,max_block)
    
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health    
        
if __name__ == "__main__":
        my_hero = Hero("Grace Hopper", 200)
        print(my_hero.name)
        print(my_hero.current_health)