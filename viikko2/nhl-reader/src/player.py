import requests

class Player:
    """Represents a hockey player."""
    def __init__(self, data):
        self.name = data['name']
        self.team = data['team']
        self.nationality = data['nationality']
        self.goals = data['goals']
        self.assists = data['assists']

    def __str__(self):
        return (f"{self.name:20}{self.team:15}{self.goals:2} + "
        f"{self.assists:2} = {self.goals + self.assists}")

class PlayerReader:
    """Reads player data from a given URL."""
    def __init__(self, url):
        self._url = url

    def get_players(self):

        response = requests.get(self._url, timeout=10)
        player_dicts = response.json()

        players = []
        for player_dict in player_dicts:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    """Provides statistics about players."""
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(
            lambda player: player.nationality == nationality,
            self._players
        )
        sorted_players = sorted(
            filtered_players,
            reverse=True,
            key=lambda player: player.goals + player.assists
        )
        return sorted_players
