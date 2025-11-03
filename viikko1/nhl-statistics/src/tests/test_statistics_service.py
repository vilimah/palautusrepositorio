import unittest
import statistics_service
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
        # korvataan statistics_service-moduulin PlayerReader stubilla
        statistics_service.PlayerReader = PlayerReaderStub
        self.stats = statistics_service.StatisticsService()

    def test_search_returns_player_if_name_exists(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
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
        names = [p.name for p in edm_players]
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)

    def test_team_returns_empty_list_if_team_does_not_exist(self):
        team = self.stats.team("NYR")
        self.assertEqual(len(team), 0)

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)
        # implementation returns how_many+1 players
        self.assertEqual(len(top_players), 4)

    def test_top_returns_players_ordered_by_points(self):
        top_players = self.stats.top(3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
        self.assertEqual(top_players[3].name, "Kurri")

    def test_top_with_zero_returns_one_player(self):
        top_players = self.stats.top(0)
        self.assertEqual(len(top_players), 1)
        self.assertEqual(top_players[0].name, "Gretzky")

if __name__ == '__main__':
    unittest.main()
