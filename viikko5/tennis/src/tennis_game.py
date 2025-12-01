class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def game_tied(self):
        return self.m_score1 == self.m_score2

    def tied_score(self):
        if self.m_score1 < 3:
            return self.score[self.m_score1] + "-All"
        else:
            return "Deuce"

    def advantage(self):
        return self.m_score1 >= 4 or self.m_score2 >= 4

    def advantage_player(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return "Advantage " + self.player1_name
        elif minus_result == -1:
            return "Advantage " + self.player2_name
        elif minus_result >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def get_score(self):
        if self.game_tied():
            return self.tied_score()
        
        if self.advantage():
            return self.advantage_player()
        
        return self.score[self.m_score1] + "-" + self.score[self.m_score2]
