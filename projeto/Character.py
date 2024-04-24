import random


class Character:
    def __init__(self, name: str, life: int, level: int) -> None:
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

    def atack(self, target: 'Character'):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_damage(damage)
        print(f"""{self.get_name()} is attacking {
              target.get_name()} with {damage} points of damage""")

    def receive_damage(self, damage: int):
        self.__life -= damage
        if (self.__life <= 0):
            self.__life = 0
