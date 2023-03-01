class Player:
    def __init__(self, name, number, position, goal, decisive, yellow_card, red_card):
        self.name = name
        self.number = number
        self.position = position
        self.goal = goal
        self.decisive = decisive
        self.yellow_card = yellow_card
        self.red_card = red_card

    def score_goal(self):
        self.goal += 1

    def make_decisive(self):
        self.decisive += 1

    def receive_yellow(self):
        self.yellow_card += 1

    def receive_red(self):
        self.red_card += 1

    def show_stats(self):
        print(f"Name: {self.name}\n"
              f"Number: {self.number}\n"
              f"Position: {self.position}\n"
              f"Goal: {self.goal}\n"
              f"Decisive: {self.decisive}\n"
              f"Yellow card: {self.yellow_card}\n"
              f"Red card: {self.red_card}\n")


class Team:
    def __init__(self, name):
        self.team_name = name
        self.player_list = []

    def add_player(self, player):
        self.player_list.append(player)

    def show_stats(self):
        print(f"Stats of {self.team_name}\n")
        for player in self.player_list:
            player.show_stats()


player1 = Player("Momo", 1, "Defender", 0, 5, 1, 0)
player2 = Player("Nico", 2, "Defence", 1, 0, 3, 0)
player3 = Player("Mama", 3, "Forward", 15, 5, 0, 0)
player4 = Player("Amoe", 4, "Defence", 1, 5, 1, 0)
player5 = Player("AZds", 5, "Sweeper", 10, 5, 3, 2)
player6 = Player("MAEF", 6, "Striker", 5, 3, 0, 0)

Team1 = Team("PSG")
Team2 = Team("OM")

Team1.add_player(player1)
Team1.add_player(player2)
Team1.add_player(player3)

Team2.add_player(player4)
Team2.add_player(player5)
Team2.add_player(player6)

Team1.show_stats()
Team2.show_stats()

player1.score_goal()
player6.receive_red()
player3.make_decisive()

Team1.show_stats()
Team2.show_stats()
