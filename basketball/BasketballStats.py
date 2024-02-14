"""
Kyle Krstulich
1/31/24
CSCI370

Analyzer must include (calculated from traditional statistics):

eFG%
Usage Rate
Fantasy Points Per Minute
Number of games to be played in the current week
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import datetime

SITE = "https://www.basketball-reference.com"


class Player:

    def __init__(self, playerUrl: str, playerName: str, numberOfGamesThisWeek: int):
        self.url = playerUrl
        self.name = playerName
        self._data = pd.read_html(self.url, dtype_backend="numpy_nullable")
        self._game_logs = self._grab_gamelogs()
        self.gameNumber = numberOfGamesThisWeek

    def _get_minuets_played(self):

        game_logs = self.get_gamelog()["MP"].apply(
            pd.to_datetime, format="%M:%S", errors="coerce").mean()
        return game_logs.minute + (game_logs.second / 60)

    def _grab_gamelogs(self):
        url = f"{self.url[:-5]}/gamelog/2024"
        return pd.read_html(url)[7]

    def get_last_five_games(self):
        return self._data[0]

    def get_per_game(self):
        return self._data[1]

    def get_per_game_playoffs(self):
        return self._data[2]

    def get_insights(self):
        return self._data[3]

    def get_totals(self):
        return self._data[4]

    def get_totals_playoffs(self):
        return self._data[5]

    def get_advanced(self):
        return self._data[6]

    def get_advanced_playoffs(self):
        return self._data[7]

    def get_gamelog(self):
        return self._game_logs

    def get_usage_rate(self):
        game_logs = self.get_gamelog().apply(pd.to_numeric, errors="coerce")
        fta = game_logs["FTA"].sum() * .44
        fga = game_logs["FGA"].sum()
        tov = game_logs["TOV"].sum()
        return fta + fga + tov

    def get_games_this_week(self):
        return self.gameNumber

    """
    The NBA's standard fantasy points scoring system dictates:

    Points = 1.0 fantasy point
    Rebounds = 1.2 fantasy points
    Assists = 1.5 fantasy points
    Steals = 3.0 fantasy points
    Blocks = 3.0 fantasy points
    Turnovers = -1.0 fantasy points
    """

    def get_points_per_min(self):
        game_logs = self.get_gamelog().apply(pd.to_numeric, errors="coerce")
        points = game_logs["PTS"].mean()
        rebounds = game_logs["TRB"].mean() * 1.2
        assists = game_logs["AST"].mean() * 1.5
        steals = game_logs["STL"].mean() * 3
        blocks = game_logs["BLK"].mean() * 3
        turnovers = game_logs["TOV"].mean()
        mean_points = (rebounds + assists + steals +
                       blocks - turnovers) / self._get_minuets_played()

        return mean_points

    def get_effective_FG_percent(self):
        game_logs = self.get_gamelog().apply(pd.to_numeric, errors="coerce")
        field_goals = game_logs["FG"].mean()
        three_points = game_logs["3P"].mean()
        attempts = game_logs["FGA"].mean()

        output = (field_goals + (three_points * .5))/attempts
        return output


class Team:
    def __init__(self, teamCode: str):
        self.teamCode = teamCode
        self._url = f"{SITE}/teams/{
            self.teamCode}/2024.html"
        self._data = pd.read_html(self._url, dtype_backend="numpy_nullable")

        self.numberGames = self._get_number_games_this_week()

    def _encode_player(self, playerName: str) -> str:
        names = playerName.split(" ")
        id = f"{names[1][0:5].lower()}{names[0][0:2].lower()}"
        return id

    def _scrape_player_url(self, playerName: str) -> str:
        playerCode = self._encode_player(playerName)
        r = requests.get(self._url)
        soup = BeautifulSoup(r.content, 'html.parser')
        content = soup.find("a", href=re.compile(playerCode)).get("href")
        return f"{SITE}{content}"

    def _get_number_games_this_week(self):
        schedule = self.get_schedule()["Date"].apply(
            pd.to_datetime, errors="coerce").dropna()
        now = datetime.datetime.now()
        games = 0

        for item in schedule:
            delta = item - now
            if 0 <= delta.days <= 7:
                games += 1

        return games

    def get_roster(self):
        return self._data[0]

    def get_per_game(self):
        return self._data[1]

    def get_totals(self):
        return self.data[2]

    def get_advanced(self):
        return self.data[3]

    def get_player(self, playerName: str) -> Player:
        url = self._scrape_player_url(playerName)
        return Player(url, playerName, self.numberGames)

    def get_schedule(self):
        url = f"{SITE}/teams/{self.teamCode}/2024_games.html"
        return pd.read_html(url)[0]


class BasketballStats:
    def __init__(self):
        pass


def main():
    testteam = Team("ATL")
    testplayer = testteam.get_player("Trae Young")
    testgamelog = testplayer.get_gamelog()
    print(testplayer.get_points_per_min())
    print(testplayer.get_usage_rate())
    print(testplayer.get_effective_FG_percent())
    print(testplayer.get_games_this_week())


if __name__ == "__main__":
    main()
