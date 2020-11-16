class Game:
    def __init__(self, teams=None):
        if teams is None:
            teams = [["white"], ["black"]]
        self.teams = teams
