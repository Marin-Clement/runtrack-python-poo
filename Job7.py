class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def bot(self):
        self.y -= 1

    def top(self):
        self.y += 1


player_1 = Character(10, 50)

print(player_1.x, player_1.y)

player_1.top()

print(player_1.x, player_1.y)

