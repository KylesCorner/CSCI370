"""
Kyle Krstulich
2/4/24
CSCI370
scraper.py

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

PLAYER_STAT_NAMES = ['date', 'team', 'opp', 'result', 'gs', 'mp', 'fg', 'fga', 'fg%', '3p', '3pa',
                     '3p%', 'ft', 'fta', 'ft%', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts', 'game_score', 'plus_minus']
PLAYER_TABLE_IDS = ['last5', 'per_game', 'totals']

TEAM_IDS = []


def player_parse(player_id):
    url = f"https://www.basketball-reference.com/players/v/{player_id}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # s = soup.find(attrs={"id": "last5"})
    # content = s.find_all(attrs={"data-stat": "game_score"})
    #
    # for item in content:
    #     print(item.string)

    s = soup.find(attrs={"id": "last5"})
    for name in PLAYER_STAT_NAMES:
        content = s.find_all(attrs={"data-stat": name})
        for item in content:
            print(item.string)


def main():
    # player_parse("vassede01")
    url = 'https://www.basketball-reference.com/players/v/vassede01.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    table = soup.find_all('table')
    dfs = pd.read_html(url)
    last5 = dfs[0]

    print(type(last5.loc[0, "PTS"]))
    dfs = pd.read_html(
        "https://www.basketball-reference.com/teams/BOS/2024.html")

    print(dfs)


if __name__ == "__main__":
    main()
