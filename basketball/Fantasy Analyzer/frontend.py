"""
Kyle Krstulich
4/2/24
CSCI370
frontend.py

"""
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import backend
from nba_api.stats.endpoints import commonplayerinfo

matplotlib.use("TkAgg")


AVG_FG_PERC = 0.475
MAX_PLAYERS = 13


class gui:
    def __init__(self, data):
        self.data = data
        if (type(data) == list):
            self.size = len(data)
        else:
            self.size = 1

        self.fig, self.axs = plt.subplots(
            ncols=self.size,
            figsize=(8, 8),
            constrained_layout=True
        )

    def get_name(self, playerFrame) -> str:
        commonPlrData = commonplayerinfo.CommonPlayerInfo(
            player_id=playerFrame["Player_ID"]).get_data_frames()[0]
        playerName = str(commonPlrData["FIRST_NAME"][0] +
                         " " + commonPlrData["LAST_NAME"][0])

        return playerName

    def get_usage_rate(self, df):
        fta = df["FTA"]*.44
        fga = df["FGA"]
        tov = df["TOV"]
        output = fta + fga + tov
        output = pd.Series(output)
        return output

    def get_points_per_min(self, df):
        points = df["PTS"]
        rebounds = df["REB"] * 1.2
        assists = df["AST"] * 1.5
        steals = df["STL"] * 3
        blocks = df["BLK"] * 3
        turnovers = df["TOV"]
        output = (points + rebounds + assists + steals + blocks - turnovers)
        output = pd.Series(output)
        return output

    def plot_data(self):
        usageRate = []
        fPoints = []

        for index in range(self.size):

            if (type(self.data) == list):
                playerName = self.get_name(self.data[index])
                usageRate = pd.DataFrame(self.get_usage_rate(self.data[index]))
                fPoints = pd.DataFrame(
                    self.get_points_per_min(self.data[index]))

                self.axs[index].hlines(
                    y=AVG_FG_PERC, xmin=0, xmax=60, color='r')
                self.axs[index].title.set_text(playerName)
                self.axs[index].plot(self.data[index]["FG_PCT"])
                self.axs[index].plot(usageRate)
                self.axs[index].plot(fPoints)
                self.axs[index].legend(
                    ["AVG FG%", "FG%", "Usage Rate", "Fantasy Points"])
            else:
                usageRate = pd.DataFrame(self.get_usage_rate(self.data))
                fPoints = pd.DataFrame(self.get_points_per_min(self.data))
                self.axs.hlines(y=AVG_FG_PERC, xmin=0, xmax=60, color='r')
                self.axs.plot(self.data["FG_PCT"])
                self.axs.plot(usageRate)
                self.axs.plot(fPoints)
                self.axs.plot()

        plt.show()


def main():
    testData = pd.read_csv("player.csv")
    g = gui(backend.get_data())
    g.plot_data()


if __name__ == "__main__":
    main()
