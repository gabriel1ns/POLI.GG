import datetime;

class Match:
    def __init__(self, champion, outcome, kills, deaths, assists, date = None):
        self.champion = champion
        self.outcome = outcome
        self.kills = kills
        self.deaths = deaths
        self.assists = assists

    def calculate_kda(self):
        if self.deaths == 0:
            return self.kills + self.assists
        return (self.kills + self.assists) / self.deaths
