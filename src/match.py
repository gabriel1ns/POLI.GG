import datetime

#definiton of the main ADT, basically all the parameters that make one LoL match.
class Match:
    def __init__(self, champion, outcome, kills, deaths, assists, items, cs, duration_minutes, date=None):
        self.champion = champion
        self.outcome = outcome
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.items = items
        self.cs = cs
        self.duration_minutes = duration_minutes
        self.date = date if date else datetime.datetime.now()

    def calculate_kda(self):
        if self.deaths == 0:
            return self.kills + self.assists
        return (self.kills + self.assists) / self.deaths