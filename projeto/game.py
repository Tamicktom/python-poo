# Character: class mother
# Hero: Controlled by the player
# Enemy: Controlled by the computer

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
        damage = self.__level * 2
        target.receive_damage(damage)
        print(f"""{self.get_name()} is attacking {
              target.get_name()} with {damage} points of damage""")

    def receive_damage(self, damage: int):
        self.__life -= damage
        if (self.__life <= 0):
            self.__life = 0


class Hero(Character):
    def __init__(self, name: str, life: int, level: int, hability: str):
        super().__init__(name, life, level)
        self.__hability = hability

    def get_hability(self):
        return self.__hability

    def show_details(self):
        return f"{super().show_details()}, Hability: {self.get_hability()}"

    def special_attack(self, target: 'Character'):
        damage = self.get_level() * 5
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

        if (self.hero.get_life() > 0):
            print("Hero won!")
        elif (self.enemy.get_life() > 0):
            print("Enemy won!")
        else:
            print("Draw!")


# Create an instance of the Game class
game = Game()
game.start_combat()
