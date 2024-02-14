"""
Kyle Krstulich
1/13/24
CSCI370
superbowl.py

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Plots:

    def __init__(self):
        self._file_path = "superbowldata.xlsx"
        self._file = pd.read_excel(io=self._file_path,
                                   skiprows=[1],
                                   parse_dates=True,
                                   date_format="%Y-%M-%D")

    def get_data(self):
        return self._file

    def print_prediction(self):
        sf = pd.read_csv("SF.csv")
        kc = pd.read_csv("KC.csv")
        points = [
            (kc["Tm"].mean(), kc["Opp"].mean()),
            (sf["Tm"].mean(), sf["Opp"].mean())
        ]
        sfAvg = round((points[0][1] + points[1][0])/2)
        kcAvg = round((points[0][0] + points[1][1])/2)

        print()
        print(f"SF Points Scored Avg: {round(points[1][0])} points")
        print(f"SF Points Allowed Avg: {round(points[1][1])} points")
        print(f"SF Points Scored/Allowed Avg: {sfAvg} points")
        print()
        print(f"KC Points Scored Avg: {round(points[0][0])} points")
        print(f"KC Points Allowed Avg: {round(points[0][1])} points")
        print(f"KC Points Scored/Allowed Avg: {kcAvg} points")
        print()

    def plot(self):
        superBowlTeams = [
            "Kansas City Chiefs",
            "San Francisco 49ers"
        ]
        fig, ax = plt.subplots()
        fig.suptitle("Football Team Comparison")

        topColors = [
            "green" if item in superBowlTeams else "black" for item in self._file.Winner]
        bottomColors = [
            "red" if item in superBowlTeams else "grey" for item in self._file.Winner
        ]

        ax.bar(x=self._file.Winner,
               height=self._file.Wpts,
               color=topColors)
        ax.bar(x=self._file.Winner,
               height=(-1 * self._file.Lpts),
               color=bottomColors)

        ax.tick_params(axis='x', labelrotation=80, labelsize=6, pad=0)

        plt.yticks(np.arange(-40, 60, 5))
        plt.ylabel("Points Scored/Allowed")
        plt.grid()
        plt.show()


def main():
    test = Plots()
    test.print_prediction()
    test.plot()


if __name__ == "__main__":
    main()
