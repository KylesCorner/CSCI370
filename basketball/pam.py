"""
Kyle Krstulich
2/28/24
CSCI370
pam.py


"""
import pandas as pd

FILE_PATH = "Template.xlsx"


def calc_pam(df):
    pamDict = {}

    for plr in df.iterrows():
        pts = plr[1]["PTS"]
        fga = plr[1]["FGA"]
        fta = plr[1]["FTA"]
        pamDict[plr[1]["Player"]] = [pts - (1.15 * (fga + (0.475 * fta)))]

    return pd.DataFrame.from_dict(pamDict)


def main():
    kingsData = pd.read_excel(FILE_PATH)
    pamData = calc_pam(kingsData)

    pamData.to_csv("kingsPam.csv")


if __name__ == "__main__":
    main()
