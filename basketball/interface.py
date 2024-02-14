"""
Kyle Krstulich
2/7/23
CSCI370
interface.py

FIXME: need to cache table values. It should be faster and not pull as many
requests.
"""

from BasketballStats import Team


def pull_data(team_and_player: tuple):
    team, player = team_and_player
    df = Team(team).get_player(player)
    print(df.get_gamelog())
    df.get_gamelog().to_csv(path_or_buf="test.csv")
    return df


def gather_input() -> list:
    file = open("input.txt", "r")
    file_lines = file.readlines()

    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i][:-1]
        file_lines[i] = tuple(file_lines[i].split(","))

    return file_lines


def get_player_summary(team_and_player):

    team, player = team_and_player
    data = pull_data(team_and_player)
    print(f"Name: {player}")
    print(f"Team: {team}")
    print(f"eFG%: {data.get_effective_FG_percent()}")
    print(f"Usage Rate: {data.get_usage_rate()}")
    print(f"Points per min: {data.get_points_per_min()}")
    print(f"Number of games this week: {data.get_games_this_week()}")
    print("-"*40)


def pick_player(user_in):
    for index, line in enumerate(user_in):
        team, player = line
        print(f"{index+1}: {player}, {team}")

    choice = int(input("Choose a player: "))
    data = user_in[choice - 1]
    get_player_summary(data)


def main():
    userin = gather_input()
    pick_player(userin)


if __name__ == "__main__":
    main()
