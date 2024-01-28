"""
Kyle Krstulich
1/25/24
PitcherClient.py
CSCI370

"""

from BaseballStats import Player


def main():

    arguments = ["Rk", "Rslt", "IP", "R", "ER",
                 "SO", "HR", "HBP", "ERA", "BF", "Pit", "Str"]
    paths = ["aronnola.csv", "zackwheeler.csv", "taijuanwalker.csv",
             "rangersuarez.csv", "christophersanchez.csv"]
    names = ["Aaron Nola", "Zack Wheeler", "Taijuan Walker",
             "Ranger Suarez", "Christopher Sanchez"]
    players = [Player(name, path, arguments)
               for path, name in list(zip(paths, names))]

    [print(player.get_name()) for player in players]


if __name__ == "__main__":
    main()
