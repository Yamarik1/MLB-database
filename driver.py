import queryList
import string
import mariadb
import sys


def main():
    isEnd = False

    while not isEnd:
        userInput = input("Enter a command (enter 'quit' to exit): ")
        splitInput = userInput.split()
        if splitInput[0].lower() == "quit" and len(splitInput) == 1:
            isEnd = True
        elif splitInput[0].lower() == "help":
            queryList.printCommand()
        elif splitInput[0].lower() == "batter":
            queryList.batterCommand()
        elif splitInput[0].lower() == "pitcher":
            queryList.pitcherCommand()
        elif splitInput[0].lower() == "team":
            queryList.teamCommand()
        elif splitInput[0].lower() == "ab":
            queryList.ABCommand()
        elif splitInput[0].lower() == "division":
            queryList.divisionCommand()
        elif splitInput[0].lower() == "league":
            queryList.leagueCommand()
        elif splitInput[0].lower() == "mlb":
            queryList.mlbCommand()
        elif splitInput[0].lower() == "game":
            queryList.endGameCommand()
        else:
            print("Invalid command\n")


main()
