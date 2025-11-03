import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # alustetaan StatisticsService käyttämään PlayerReaderStub-luokkaa
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_returns_player_if_name_exists(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)
    
    def test_search_returns_none_if_name_does_not_exist(self):
        player = self.stats.search("Selanne")
        self.assertIsNone(player)
    
    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        
        self.assertEqual(len(edm_players), 3)
        player_names = [player.name for player in edm_players]
        self.assertIn("Semenko", player_names)
        self.assertIn("Kurri", player_names)
        self.assertIn("Gretzky", player_names)
    
    def test_team_returns_empty_list_if_team_does_not_exist(self):
        team = self.stats.team("NYR")
        self.assertEqual(len(team), 0)
    
    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4) 
    
    def test_top_returns_players_ordered_by_points(self):
        top_players = self.stats.top(3)
        
        self.assertEqual(top_players[0].name, "Gretzky")  # 35 + 89 = 124 points
        self.assertEqual(top_players[1].name, "Lemieux")  # 45 + 54 = 99 points
        self.assertEqual(top_players[2].name, "Yzerman")  # 42 + 56 = 98 points
        self.assertEqual(top_players[3].name, "Kurri")    # 37 + 53 = 90 points
    
    def test_top_with_zero_returns_one_player(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_by_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(top_players[0].name, "Lemieux")  # 45 goals
        self.assertEqual(top_players[1].name, "Yzerman")  # 42 goals

    def test_top_by_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")   # 89 assists
        self.assertEqual(top_players[1].name, "Yzerman")   # 56 assists