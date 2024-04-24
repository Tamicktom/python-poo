import random
from Character import Character


class Hero(Character):
    def __init__(self, name: str, life: int, level: int, hability: str):
        super().__init__(name, life, level)
        self.__hability = hability

    def get_hability(self):
        return self.__hability

    def show_details(self):
        return f"{super().show_details()}, Hability: {self.get_hability()}"

    def special_attack(self, target: 'Character'):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_damage(damage)
        print(f"""{self.get_name()} is attacking {
              target.get_name()} with {damage} points of damage""")


class Enemy(Character):
    def __init__(self, name: str, life: int, level: int, type: str):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}, Type: {self.get_type()}"


class Game:
    """ Class Orchestrator of the game """

    def __init__(self):
        self.hero = Hero('Hero', 100, 5, 'Fly')
        self.enemy = Enemy('Enemy', 100, 1, 'Orc')

    def start_combat(self):
        """ Make the hero attack the enemy """
        print("Combat started")

        is_hero_alive = self.hero.get_life() > 0
        is_enemy_alive = self.enemy.get_life() > 0

        while is_hero_alive and is_enemy_alive:
            print("\nCharacters status:")
            print(self.hero.show_details())
            print(self.enemy.show_details())

            input("\nPress Enter to attack the enemy")
            choice = input(
                "Choose the type of attack (1 - Basic, 2 - Special): ")

            if choice == '1':
                self.hero.atack(self.enemy)
                self.enemy.atack(self.hero)
            elif choice == '2':
                self.hero.special_attack(self.enemy)
                self.enemy.atack(self.hero)
            else:
                print("Invalid option")

            is_hero_alive = self.hero.get_life() > 0
            is_enemy_alive = self.enemy.get_life() > 0

        if (self.hero.get_life() > 0):
            print("Hero won!")
        elif (self.enemy.get_life() > 0):
            print("Enemy won!")
        else:
            print("Draw!")


# Create an instance of the Game class
game = Game()
game.start_combat()
