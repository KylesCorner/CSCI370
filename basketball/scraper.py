"""
Kyle Krstulich
2/4/24
CSCI370
scraper.py

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

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
    playerName = ["Paul", "Reed"]
    playerid = f"{playerName[1][0:5].lower()}{playerName[0][0:2].lower()}"
    url = 'https://www.basketball-reference.com/teams/PHI/2024.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.select(f"a[href*={playerid}]")
    content = soup.find("a", href=re.compile(playerid))
    print(content.get("href"))


if __name__ == "__main__":
    main()
