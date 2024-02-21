"""
Kyle Krstulich
2/14/24
CSCI370
threepoint.py


Due to the three point explosion, the average amount of points scored has
dramatically increased. Nearly double from before the rule change. The amount of
free throws has dramatically decreased sense the rule change.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = "seasondata.csv"


class Plots:
    def __init__(self):
        self.data = pd.read_csv(FILE_PATH, skiprows=[0])
        self.fig, self.axs = plt.subplots(2, 2)

    # TODO: label axis's
    def plot(self):

        self.axs[0][0].plot(self.data["eFG%"])
        self.axs[0][0].set_title("eFG%")
        self.axs[0][0].set_xlabel("Years after 1957")
        self.axs[0][0].set_ylabel("Points")
        self.axs[0][0].invert_xaxis()

        self.axs[0][1].plot(self.data["FT"])
        self.axs[0][1].set_title("FT")
        self.axs[0][1].set_xlabel("Years after 1957")
        self.axs[0][1].set_ylabel("Points")
        self.axs[0][1].invert_xaxis()

        self.axs[1][0].plot(self.data["3P"])
        self.axs[1][0].set_title('3P')
        self.axs[1][0].set_xlabel("Years after rule change")
        self.axs[1][0].set_ylabel("Points")
        self.axs[1][0].invert_xaxis()

        self.axs[1][1].plot(self.data["3PA"])
        self.axs[1][1].set_title("3PA")
        self.axs[1][1].set_xlabel("Years after rule change")
        self.axs[1][1].set_ylabel("Points")
        self.axs[1][1].invert_xaxis()

        plt.show()


def main():
    test = Plots()
    test.plot()


if __name__ == "__main__":
    main()
