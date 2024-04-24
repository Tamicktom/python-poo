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


hero = Hero('Hero', 100, 5, 'Fly')
enemy = Enemy('Enemy', 100, 1, 'Orc')

print(hero.show_details())
print(enemy.show_details())
