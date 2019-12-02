import random

class Ability:

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        rand_hit = random.randint(0,self.max_damage)
        return rand_hit

class Weapon(Ability):
    def attack(self):
        weapon_attack = random.randint(self.max_damage//2, self.max_damage)
        return weapon_attack

class Nuclear(Weapon):
    """A weapon that damages both hero and oppponent"""
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        self.is_nuclear = True

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        rand_block = random.randint(0, self.max_block)
        return rand_block
    
class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health   
        self.deaths = 0
        self.kills = 0
        self.status = "Alive"
        
    def add_ability(self, ability):
        self.abilities.append(ability)
        print('{} now has {}.'.format(self.name, ability.name))
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print('{} now has {}.'.format(self.name, weapon.name))

    # def add_bomb(self, nuclear):
    #     self.abilites.append(nuclear)
    #     print('{} now has {}.'.format(self.name, nuclear.name))

    def attack(self):

        damage = 0
        for ability in self.abilities:
            dmg = ability.attack()
            print(f'{self.name} attacking with {ability.name} for {dmg} damage.')
            damage += dmg
            print('{} | {}'.format(ability.name, damage))
            # if ability.is_nuclear:
            #     self_damage = ability.attack()
            #     print(f'Damaged self flr {self_damage} damage!')
            #     self.take_damage(self_damage)
        return damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt):
        total_block = 0
        for armor in self.armors:
            bl = armor.block()
            print(f'Up to {bl} damage blocked with {armor.name}.')
            total_block += bl
        return total_block

    def take_damage(self, damage):
        defense = self.defend(50)-damage
        if defense < 0:
            self.current_health += defense

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else: 
            return True

    def revive(self):
        self.current_health = self.starting_health

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
        print('{} now has {}.'.format(self.name, weapon.name))



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
            if hero.deaths != 0:
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

class Arena:
    def __init__(self):
        # self.username = username
        self.team_one = Team(" One ")
        self.team_two = Team(" Two ")

    def create_ability(self):
        ability_name = input("What is the ability?  ").title()
        ability_max_dam = ''
        while not ability_max_dam .isnumeric():
           ability_max_dam = input('Max. damage of this ability?: ')
        ability_max_dam = int(ability_max_dam)
        return Ability(ability_name, ability_max_dam)

    def create_weapon(self):
        weapon_name = input("What weapon does this hero use? ").title()
        weapon_max_dam = ''
        while not weapon_max_dam.isnumeric():
            weapon_max_dam = input("What is the max damage of the weapon? ")
        weapon_max_dam = int(weapon_max_dam)
        return Weapon(weapon_name, weapon_max_dam)

    def create_armor(self):
        armor_name = input("What kind of armor does this hero use?: ").title()
        armor_power = ''
        while not armor_power.isnumeric():
            armor_power = input("What's the blocking power of this armor?: ")
        armor_power = int(armor_power)
        return Armor(armor_name, armor_power)

    def create_hero(self):
        hero_name = input("Hero's name: ").title()
        hero = Hero(hero_name)
        hero_health = ''
        while not hero_health.isnumeric():
            hero_health = input("What's our hero's maximum health?: ")
        hero_health = int(hero_health)
        hero = Hero(hero_name, hero_health)

        abilities_count = ''
        while not abilities_count.isnumeric():
            abilities_count = input("Number of abilities: ")
        abilities_count = int(abilities_count)
        for x in range(0, abilities_count):
            hero.add_ability(self.create_ability())

        weapons_count = ''
        while not weapons_count.isnumeric():
            weapons_count = input("How many weapons?: ")
        weapons_count = int(weapons_count)
        for x in range(0, weapons_count):
            hero.add_weapon(self.create_weapon())

        armors_count = ''
        while not armors_count.isnumeric():
            armors_count = input("How many pieces of armor does this hero wear?: ")
        armors_count = int(armors_count)
        for x in range(0, armors_count):
            hero.add_armor(self.create_armor())
            
        return hero

    def build_team_one(self):
        name = input("Team 1 Name: ")
        num_of_heroes = int(input("How many heroes?: "))
        self.build_team_one = Team(name)

        for i in range(num_of_heroes):
            hero = self.create_hero()
            self.build_team_one.add_hero(hero)
        
        self.build_team_one.view_all_heroes()

    def build_team_two(self):
        name = input("Team 2 Name: ")
        num_of_heroes = int(input("How many heroes?: "))
        self.build_team_two = Team(name)

        for i in range(num_of_heroes):
            hero = self.create_hero()
            self.build_team_two.add_hero(hero)
        
        self.build_team_two.view_all_heroes()
       
    # Method that has the two teams fight each other
    def team_battle(self):
        self.winning_team = self.build_team_one.attack(self.build_team_two)
    
    # Method that prints who won the fight and the stats of each Hero on both teams; also shows any surviving Heroes
    def show_stats(self):
        print("The winners are: " + self.winning_team)
        
        self.build_team_one.stats()
        self.build_team_two.stats()

        if self.winning_team == self.build_team_one.name:
            for hero in self.build_team_one.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)
        elif self.winning_team == self.build_team_two.name:
            for hero in self.build_team_two.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()