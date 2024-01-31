"""
Kyle Krstulich
1/25/24
BaseballStats.py
CSCI370



Name ,Rank(R), Game Results(Rslt), Innings Pitched(IP), Runs Scored/Allowed(R),
Earned Runs Allowed(ER),Strikeouts(SO), Home Runs(HR), Times hit by pitch(HBP),
9*ER/IP(ERA), Batters Faced(BF), Number of Pitches(Pit), Strikes(Str)
"""


import pandas as pd
import numpy as np
import math


class Player:
    def __init__(self, playerName: str, pathToCsv: str, arguments: list):
        # TODO check for correct path
        with open(pathToCsv, newline='') as csvfile:
            self._data = pd.read_csv(
                pathToCsv, parse_dates=True, skipfooter=1)
            csvfile.close()

        self._arguments = arguments
        self._blacklistedItems = []

        self.playerName = playerName

        if (len(self._arguments) > 0):
            self._satisfy_arguments()

    # -----------------------
    # Private Methods
    # -----------------------

    def _satisfy_arguments(self):
        for key in self._data.columns:
            if key not in self._arguments:
                self._blacklistedItems.append(self._data.pop(key))

    # -----------------------
    # Public Methods
    # -----------------------

    def get_blacklisted_items(self) -> list:
        return self._blacklistedItems

    def get_name(self) -> str:
        return self.playerName

    def get_group_data(self, labels: list):
        for key in self._data.columns:
            if key not in labels:
                self._blacklistedItems.append(self._data.pop(key))


class BaseballStats:

    def __init__(self, Players: list):
        self.plrs = Players

    def get_pitches_vs_onbase(self):
        result = []
        labels = ["SO", "BF", "Pit", "R"]

        for plr in self.plrs:
            temp_data = 0
            size = plr._data.shape[0]

            for index in range(1, size):
                S = plr._data.loc[index, labels[0]]
                B = plr._data.loc[index, labels[1]]
                P = plr._data.loc[index, labels[2]]
                R = plr._data.loc[index, labels[3]]

                W = P * (R/math.pow((B - S), 2))
                temp_data += W

            result.append((plr.playerName, np.tanh(W/size)))

        return result


def main():
    # plr = Player("testing", "zackwheeler.csv", ["Rk", "Rslt", "Pit"])
    plr = Player("testing", "zackwheeler.csv", [])
    bs = BaseballStats([plr])
    plr.get_group_data(["SO", "BF", "Pit", "R"])
    print(plr._data)
    print(bs.get_pitches_vs_onbase())


if __name__ == "__main__":
    main()
