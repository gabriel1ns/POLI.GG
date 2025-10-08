from replayQueue import ReplayQueue
from replaySorting import merge_sort
from LinkedList import LinkedList

class HistoryAnalyzer:
    #instaciating match history and vod review queue.
    def __init__(self):
        self.match_history = LinkedList()
        self.replay_queue = ReplayQueue()

    def add_match(self, match):
        self.match_history.append(match) #append defined on LinkedList.py

    def get_sorted_history(self, sort_by='date'):
        if len(self.match_history) == 0:
            return []
        
        matches = list(self.match_history)
        return merge_sort(matches, sort_by) #return sorted lists of the chosen category

    def analyze_champion_performance(self, champ_name):
        matches = list(self.match_history)
        
        #simple pyhon list to store the matches to be used in analysis
        champ_matches = []
        for m in matches:
            if m.champion.lower() == champ_name.lower():
                champ_matches.append(m)

        if len(champ_matches) == 0:
            return None

        total = len(champ_matches)
        wins = 0
        total_kills = 0
        total_deaths = 0
        total_assists = 0
        total_kda = 0
        
        for m in champ_matches:
            if m.outcome == "Victory":
                wins += 1
            total_kills += m.kills
            total_deaths += m.deaths
            total_assists += m.assists
            total_kda += m.calculate_kda()
        
        stats = {
            "total_matches": total,
            "victories": wins,
            "win_rate": (wins / total) * 100,
            "avg_kills": total_kills / total,
            "avg_deaths": total_deaths / total,
            "avg_assists": total_assists / total,
            "avg_kda_ratio": total_kda / total
        }
        
        sorted_matches = merge_sort(champ_matches, 'date')
        
        return stats, sorted_matches

    def add_to_replay_queue(self, match):
        self.replay_queue.enqueue(match)

    def process_next_in_queue(self):
        return self.replay_queue.dequeue()