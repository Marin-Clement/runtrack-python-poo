import random

class Personnage:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, opponent):
        attack_points = random.randint(10, 20)
        opponent.health -= attack_points
        print(f"{self.name} attacks {opponent.name} and removes {attack_points} health points.")

    def is_alive(self):
        return self.health > 0


class Game:
    def choose_level(self):
        levels = {
            1: {"player_health": 100, "enemy_health": 100},
            2: {"player_health": 100, "enemy_health": 150},
            3: {"player_health": 150, "enemy_health": 200}
        }
        while True:
            level = int(input("Choose a difficulty level (1-3): "))
            if level in levels:
                self.level = level
                self.player_health = levels[level]["player_health"]
                self.enemy_health = levels[level]["enemy_health"]
                break
            else:
                print("Invalid level. Please choose a level between 1 and 3.")

    def start_game(self):
        self.choose_level()
        player = Personnage("Player", self.player_health)
        enemy = Personnage("Enemy", self.enemy_health)
        print(
            f"A battle begins between {player.name} ({player.health} health points) and {enemy.name} ({enemy.health} health points).")
        while player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            if not enemy.is_alive():
                break
            enemy.attack(player)
        if player.is_alive():
            print(f"{player.name} has defeated {enemy.name}!")
        else:
            print(f"{enemy.name} has defeated {player.name}!")


game = Game()
game.start_game()
