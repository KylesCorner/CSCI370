"""
Kyle Krstulich
4/1/24
CSCI370
backend.py


"""
from nba_api.stats.endpoints import playergamelog


def read_config():
    file = open("config.txt", "r")
    lines = file.readlines()
    lines = ''.join(lines).split('=')[1].split(',')
    lines = [entry.strip() for entry in lines]
    return lines


def get_data():
    ids = read_config()
    data = [playergamelog.PlayerGameLog(id).get_data_frames()[0] for id in ids]
    return data


def get_singleton():
    ids = read_config()
    data = playergamelog.PlayerGameLog(ids[0]).get_data_frames()[0]
    data.to_csv("player.csv")


def main():
    get_singleton()


if __name__ == "__main__":
    main()
