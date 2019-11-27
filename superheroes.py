import random

class Ability:

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        rand_hit = random.randint(0,self.max_damage)
        return rand_hit

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        rand_block = random.randint(0, self.max_block)
        return rand_block
    
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health   
        self.deaths = 0
        self.kills = 0
        self.status = "Alive"
        
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

    def take_damage(self, damage):
        defense = self.defend(damage)
        self.current_health -= damage - defense

    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
    
    def fight(self, opponent):
        fighting = True
        while fighting == True:
            if self.abilities == None:
                return "Draw"
                fighting = False
            else:
                hero1_attack = self.attack()
                hero2_attack = opponent.attack()

                hero1_defense = self.defend(1)
                hero2_defense = opponent.defend(1)

                self.take_damage(hero2_attack)
                opponent.take_damage(hero1_attack)

            if self.is_alive() == False:
                opponent.add_kill(1)
                self.add_deaths(1)
                self.status = "Dead"
                opponent.status = "Alive"
                print(opponent.name + " won!")
                fighting = False
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_deaths(1)
                opponent.status = "Dead"
                self.status = "Alive"
                print(self.name + " won!")
                fighting = False
            # else: 
            #     fighting = True


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 380)
    ability4 = Ability("Wizard Beard", 220)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)