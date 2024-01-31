"""
Kyle Krstulich
1/25/24
PitcherClient.py
CSCI370

"""

import BaseballStats as bs


def main():

    arguments = ["Rk", "Rslt", "IP", "R", "ER",
                 "SO", "HR", "HBP", "ERA", "BF", "Pit", "Str"]
    paths = ["aronnola.csv", "zackwheeler.csv", "taijuanwalker.csv",
             "rangersuarez.csv", "christophersanchez.csv"]
    names = ["Aaron Nola", "Zack Wheeler", "Taijuan Walker",
             "Ranger Suarez", "Christopher Sanchez"]
    players = [bs.Player(name, path, arguments)
               for path, name in list(zip(paths, names))]

    stats = bs.BaseballStats(players)

    [print(player.get_name()) for player in players]
    print(stats.get_pitches_vs_onbase())


if __name__ == "__main__":
    main()
