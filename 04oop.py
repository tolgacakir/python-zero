class Team:
    def __init__(self, name, players, stadium="Ali Sami Yen Stadium"):
        self.name = name
        self.players = players
        self.stadium = stadium
    def display(self):
        print(f"Team: {self.name}")
        print(f"Stadium: {self.stadium}")
        print("Players:")
        for player in self.players:
            player.display()

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Player: {self.name}, Position: {self.position}")


# Example usage
team = Team("Galatasaray", [
    Player("Osimhen", "Forward"),
    Player("Yunus Akgün", "Midfielder"),
    Player("Mauro Icardi", "Forward")])

team.display()

# Adding a new player
new_player = Player("Davinson Sanchez", "Defender")
team.add_player(new_player)

team.stadium = "Rams Park Ali Sami Yen Stadium"
