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
            else: 
                fighting = True

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            hero.status = "Alive"

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            if hero.status == "Alive":
                living_heroes.append(self.heroes.index(hero))

        for hero in other_team.heroes:
            living_opponents.append(other_team.heroes.index(hero))

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero_1 = self.heroes[random.choice(living_heroes)]
            random_hero_2 = other_team.heroes[random.choice(living_opponents)]

            random_hero_1.fight(random_hero_2)

            for alivecheck_1 in self.heroes:
                if alivecheck_1.status == "Dead":
                    living_heroes.pop(self.heroes.index(alivecheck_1))

            for alivecheck_2 in other_team.heroes:
                if alivecheck_2.status == "Dead":
                    living_opponents.pop(other_team.heroes.index(alivecheck_2))

        if len(living_heroes) > 0:
            return self.name
        elif len(living_opponents) > 0:
            return other_team.name 
        elif len(living_heroes) == len(living_opponents):
            return "Draw!"


            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())