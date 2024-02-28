"""
2/28/24
Kyle Krstulich
montanaBB.py
CSCI370


"""

import pandas as pd
import matplotlib.pyplot as plt

MSU_PATH = "msu.csv"
UM_PATH = "umt.csv"


def get_attempts(frame):
    total = 0
    for item in frame:
        total += float(item.split("-")[0])

    return total


def get_team_poss(df):
    fga = get_attempts(df["FG"])
    fta = get_attempts(df["FT"]) + get_attempts(df["3PT"])
    orb = get_attempts(df["ORB-DRB"])
    to = sum(df["TO"])

    poss = fga + 0.475 * fta - orb + to

    return poss


# ts, % of shots, true possesion
def get_plr_poss(df):
    poss_dict = {}

    for item in df[:-2].iterrows():
        min = float(item[1]["MIN"])
        if (min >= 10):
            fga = float(item[1]["FG"].split("-")[0]) + \
                float(item[1]["3PT"].split("-")[0])
            fta = float(item[1]["FT"].split("-")[0])
            orb = float(item[1]["ORB-DRB"].split("-")[0])
            to = float(item[1]["TO"])
            pts = [
                float(item[1]["FG"].split("-")[1]),
                float(item[1]["FT"].split("-")[1]),
                float(item[1]["3PT"].split('-')[1])

            ]
            att = [
                fga, fta
            ]

            poss = fga + 0.475 * fta - orb + to
            ts = (.5 * sum(pts))/(fga + .475 * fta)

            poss_dict[item[1]["Player"]] = [ts, sum(pts)/sum(att), poss]

    return pd.DataFrame.from_dict(poss_dict)


def plot_data(umDF, msuDF):
    fig, axs = plt.subplots(2)
    x = umDF.loc[0]
    y = umDF.loc[1]
    axs[0].set_xlabel("% of shots")
    axs[0].set_ylabel("TS%")
    axs[0].set_title("UMT")
    axs[0].scatter(x, y, color="brown")

    for index, plr in enumerate(umDF):
        axs[0].annotate(plr, (x[index], y[index]))

    x = msuDF.loc[0]
    y = msuDF.loc[1]
    axs[1].set_xlabel("% of shots")
    axs[1].set_ylabel("TS%")
    axs[1].set_title("MSU")
    axs[1].scatter(x, y, color="yellow")

    for index, plr in enumerate(msuDF):
        axs[1].annotate(plr, (x[index], y[index]))

    plt.savefig("MSUvsUM.png")
    plt.show()


def main():
    msuDF = pd.read_csv(MSU_PATH, sep="	")
    umtDF = pd.read_csv(UM_PATH, sep="	")

    umPlrPoss = get_plr_poss(umtDF)
    msuPlrPoss = get_plr_poss(msuDF)

    print(umPlrPoss)
    print(msuPlrPoss)
    plot_data(umPlrPoss, msuPlrPoss)


if __name__ == "__main__":
    main()
