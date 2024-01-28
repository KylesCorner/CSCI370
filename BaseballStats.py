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


class BaseballStats:
    def __init__(self):
        pass


def main():
    # plr = Player("testing", "zackwheeler.csv", ["Rk", "Rslt", "Pit"])
    plr = Player("testing", "zackwheeler.csv", [])
    print(plr._data)


if __name__ == "__main__":
    main()
