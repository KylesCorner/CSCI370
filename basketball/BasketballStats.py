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
import numpy as np
import pandas as pd
import requests
import urllib


class Player:

    def __init__(self, playerName: str):
        self.playerName = playerName
        self._playerCode = self._decode_player()
        self._url = f"https://www.basketball-reference.com/players/{
            self._playerCode[0]}/{self._playerCode}.html"
        self._data = pd.read_html(self._url)

    """
     this doesnt work as intended. the reference to the player should be handled through the team class
     there is an href attribute that can be sorted through with regular
     expressions simply
    """

    def _decode_player(self) -> str:
        names = self.playerName.split(" ")
        id = f"{names[1][0:5].lower()}{names[0][0:2].lower()}01"
        return id


class Team:
    def __init__(self, teamCode: str):
        self.teamCode = teamCode
        self._url = f"https://www.basketball-reference.com/teams/{
            self.teamCode}/2024.html"
        self._data = pd.read_html(self._url)

    def get_roster(self):
        return self._data[0]


class BasketballStats:
    def __init__(self):
        pass


def main():
    testplayer = Player("Jayson Tatum")
    testteam = Team("BOS")

    print(testteam._data[1])


if __name__ == "__main__":
    main()
