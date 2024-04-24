# Character: class mother
# Hero: Controlled by the player
# Enemy: Controlled by the computer

class Character:
    def __init__(self, name, life, level) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Name: {self.get_name()}, Life: {self.get_life()}, Level: {self.get_level()}"


class Hero(Character):
    def __init__(self, name, life, level, hability):
        super().__init__(name, life, level)
        self.__hability = hability

    def get_hability(self):
        return self.__hability

    def show_details(self):
        return f"{super().show_details()}, Hability: {self.get_hability()}"


class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}, Type: {self.get_type()}"


class Game:
    """ Class Orchestrator of the game """

    def __init__(self):
        self.__hero = Hero('Hero', 100, 5, 'Fly')
        self.__enemy = Enemy('Enemy', 100, 1, 'Orc')

    def start_combat(self):
        """ Make the hero attack the enemy """
        print("Combat started")

        is_hero_alive = self.__hero.get_life() > 0
        is_enemy_alive = self.__enemy.get_life() > 0

        while is_hero_alive and is_enemy_alive:
            print("\nCharacters status:")
            print(self.__hero.show_details())
            print(self.__enemy.show_details())

            input("\nPress Enter to attack the enemy")
            choice = input(
                "Choose the type of attack (1 - Basic, 2 - Special): ")


# Create an instance of the Game class

game = Game()
game.start_combat()