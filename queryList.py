import queries


def printCommand():
    print("Here is a list of the commands you can use: ")
    print("\t- Batter: Used to get information about a certain batter")
    print("\t- Pitcher: Used to get information about a certain pitcher")
    print("\t- Manager: Used to get information about a certain teams manager")
    print("\t- Team: Used to get information about a team and its players")
    print("\t- Division: Used to get the standings of a division")
    print("\t- League: Used to get the standings of a league")
    print("\t- MLB: Used to get the standings of the entire MLB")
    print("\t- AB: Used to input the result of an At bat. Data will be updated with the information given")
    print("\t- Game: Used to input the result of a game ending, such as teams an pitchers involved")


def batterCommand():
    playerName = input("What batter would you like to look up? (First and last name): ")
    queries.batterQuery(playerName)
    return 0


def pitcherCommand():
    playerName = input("What pitcher would you like to look up? (First and last name): ")
    queries.pitcherQuery(playerName)
    return 0


def teamCommand():
    teamName = input("What team would you like to look up? (Use PascalCase if team or city name has >1 word; i.e "
                     "New York should be NewYork): ")
    queries.teamQuery(teamName)
    return 0


def ABCommand():
    print("Here is the format that should be used for the at bat")
    print("\'Batter, Pitcher, Result, RBIs\'")
    print("Result should be one of the following:\n"
          "1B, 2B, 3B, HR, FC, BB, K, HBP, E, O")
    AtBat = input("Please input the result of the at bat: ")

    splitAB = AtBat.split(',')
    queries.ABQuery(splitAB)


def divisionCommand():
    division = input("Which division would you like to see? (Ex: 'AL East'): ")
    queries.divisionQuery(division)


def leagueCommand():
    league = input("Which league would you like to see (AL or NL): ")
    queries.leagueQuery(league)


def mlbCommand():
    queries.mlbQuery()


def endGameCommand():
    print("Input the result of a game in the following format:")
    print("Winning Team, Away Team, Winning pitcher, Losing pitcher, Saving pitcher (If there is one)")

    game = input("Input the result: ")
    queries.gameQuery(game)
