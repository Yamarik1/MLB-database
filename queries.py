import connect


def batterQuery(name):
    conn = connect.connectDatabase()

    cur = conn.cursor()

    # print("player Name: " + name)
    query = "SELECT Name, At_bat, Hits, Bat_avg, RBI, Home_runs, Walks FROM batter WHERE name=\'" + name + "\';"

    cur.execute(query)

    for (name, AB, Hit, Avg, RBI, HR, BB) in cur:
        print("Name: " + str(name) + "\nAB: " + str(AB) + "\nHits: " + str(Hit) + "\nAvg: " + str(Avg))
        print("RBI: " + str(RBI) + "\nHR: " + str(HR) + "\nBB: " + str(BB))

    return 0


def pitcherQuery(name):
    conn = connect.connectDatabase()

    cur = conn.cursor()

    # print("player Name: " + name)
    query = "SELECT Name, Games_pitched, Wins, Loses, Saves, Batters_faced, Strikeouts, Opp_avg, IP,  ERA FROM pitcher " \
            "WHERE name=\'" + name + "\';"

    cur.execute(query)

    for (name, GP, W, L, S, BF, K, Avg, IP, ERA) in cur:
        print("Name: " + str(name) + "\nGames Pitched: " + str(GP) + "\nWins: " + str(W) + "\nLoses: " + str(L))
        print("Saves: " + str(S) + "\nBatters faced: " + str(BF) + "\nStrikeouts: " + str(K))
        print("Opponent average: " + str(Avg) + "\nIP: " + str(IP) + "\nERA: " + str(ERA))

    return 0


def teamQuery(name):
    split_name = name.split()

    conn = connect.connectDatabase()

    cur = conn.cursor()

    query1 = "SELECT city, Team_name, year, wins, loses FROM team WHERE Team_name =\'" + split_name[1] + "\';"

    cur.execute(query1)

    for (city, name, year, wins, losses) in cur:
        print("City Name: " + str(city) + "; Team Name: " + str(name) + "; Year founded: " + str(year))
        print("Record: " + str(wins) + "-" + str(losses))

    query2 = "SELECT team.city, team.Team_name, batter.name, batter.position FROM batter INNER JOIN team ON " \
             "batter.tID = team.tID WHERE Team_name = ? "

    cur.execute(query2, (split_name[1],))

    print("\nHere is a list of the Batters on this team")
    print("Using Format: City Name, Team Name, Player Name, Position\n")

    for city, tName, bName, pos in cur:
        print(str(city) + " " + str(tName) + "\t" + str(bName) + "\t" + str(pos))

    query3 = "SELECT team.city, team.Team_name, pitcher.name FROM pitcher INNER JOIN team ON pitcher.tID = team.tID " \
             "WHERE Team_name = ?"

    print("\nHere is a list of the Pitchers of the team\n")

    cur.execute(query3, (split_name[1],))

    for city, tName, pName in cur:
        print(str(city) + " " + str(tName) + "\t" + str(pName) + "\tP")

    query4 = "SELECT team.city, team.Team_name, manager.Name, manager.Wins, manager.Loses FROM manager INNER JOIN " \
             "team ON manager.tID = team.tID WHERE Team_name = ?;"

    print("\nHere the manager for the selected team, and their career record\n")
    cur.execute(query4, (split_name[1],))

    for (city, tName, mName, wins, loss) in cur:
        print(str(city) + " " + str(tName) + "\t" + str(mName) + " : " + str(wins) + "-" + str(loss))

    cur.close()


def ABQuery(atBat):
    if len(atBat) != 4:
        print("Invalid input")
        return 0

    batter = atBat[0].strip()
    pitcher = atBat[1].strip()
    result = atBat[2].strip()
    RBI = int(atBat[3])

    batUpdate = ""
    newHits = 0
    newRBI = 0
    newAB = 0
    newAvg = 0
    newHR = 0
    newBB = 0

    newBat = 0
    newHitsP = 0
    newAvgP = 0
    newER = 0
    newERA = 0
    newIP = 0
    newK = 0
    pitchUpdate = ""

    # A hit which is not a home run.
    if (result == "1B") or (result == "2B") or (result == "3B"):

        conn = connect.connectDatabase()
        cur = conn.cursor(buffered=True)
        batQuery = "SELECT Name, At_bat, Hits, RBI FROM batter WHERE name =\'" + batter + "\';"

        cur.execute(batQuery)
        qResult = cur.fetchall()
        for name, AB, Hits, currRBI in qResult:
            newAB = AB + 1
            newHits = Hits + 1
            newRBI = currRBI + RBI
            newAvg = round(newHits / newAB, 3)

            batUpdate = "UPDATE batter SET At_bat = ?, Hits = ?, Bat_avg = ?, RBI = ? WHERE Name = ?"

        if batUpdate == "":
            print("Invalid query")
            return 0

        cur.execute(batUpdate, (newAB, newHits, newAvg, newRBI, batter))

        conn.commit()
        cur.close()
        conn.close()

        connection = connect.connectDatabase()
        cur2 = connection.cursor(buffered=True)
        pitchQuery = "SELECT Name, Batters_faced, Hits, IP, Earned_runs, ERA FROM pitcher WHERE name = ?"
        cur2.execute(pitchQuery, (pitcher,))
        qResult = cur2.fetchall()
        cur2.close()

        cur2 = connection.cursor()
        for Name, Bat, Hits, IP, currER, ERA in qResult:
            newBat = Bat + 1
            newHitsP = Hits + 1
            newER = currER + RBI

            # Inning pitches is weirdly stored as .1 for a third, .2 for two thirds, and .0 for a full inning
            # This bit of code just turns that value into something useful for finding ERA.
            if ((IP * 10) % 10) == 0:
                actualIP = IP
            elif (((IP - .1) * 10) % 10) == 0:
                actualIP = (IP - .1) + .33
            else:
                actualIP = (IP - .2) + .66

            # ERA is (Earned runs * 9) / Total innings pitched
            newERA = round((newER * 9) / actualIP, 2)
            newAvgP = round(newHitsP / newBat, 3)
            pitchUpdate = "UPDATE pitcher SET Batters_faced = ?, Hits = ?, Opp_avg = ?, Earned_runs = ?, ERA = ? WHERE" \
                          " name = ?"

        if pitchUpdate == "":
            print("Invalid Command")
            return 0

        cur2.execute(pitchUpdate, (newBat, newHitsP, newAvgP, newER, newERA, pitcher,))

        connection.commit()
        cur2.close()
        connection.close()

    elif result == "HR":

        conn = connect.connectDatabase()
        cur = conn.cursor(buffered=True)
        batQuery = "SELECT At_bat, Hits, RBI, Home_runs FROM batter WHERE name =\'" + batter + "\';"

        cur.execute(batQuery)

        for AB, Hits, currRBI, HR in cur:
            newAB = AB + 1
            newHits = Hits + 1
            newRBI = currRBI + RBI
            newHR = HR + 1
            newAvg = round(newHits / newAB, 3)

            batUpdate = "UPDATE batter SET At_bat = ?, Hits = ?, Bat_avg = ?, RBI = ?, Home_runs = ? WHERE Name = ?"

        if batUpdate == "":
            print("Invalid query")
            return 0

        cur.execute(batUpdate, (newAB, newHits, newAvg, newRBI, newHR, batter))

        conn.commit()
        cur.close()
        conn.close()

        connection = connect.connectDatabase()
        cur2 = connection.cursor(buffered=True)
        pitchQuery = "SELECT Name, Batters_faced, Hits, IP, Earned_runs, ERA FROM pitcher WHERE name = ?"
        cur2.execute(pitchQuery, (pitcher,))
        qResult = cur2.fetchall()
        cur2.close()

        cur2 = connection.cursor()
        for Name, Bat, Hits, IP, currER, ERA in qResult:
            newBat = Bat + 1
            newHitsP = Hits + 1
            newER = currER + RBI

            # Inning pitches is weirdly stored as .1 for a third, .2 for two thirds, and .0 for a full inning
            # This bit of code just turns that value into something useful for finding ERA.
            if (IP * 10 % 10) == 0:
                actualIP = IP
            elif (((IP - .1) * 10) % 10) == 0:
                actualIP = (IP - .1) + .33
            else:
                actualIP = (IP - .2) + .66
            # ERA is (Earned runs * 9) / Total innings pitched
            newERA = round((newER * 9) / actualIP, 2)
            newAvgP = round(newHitsP / newBat, 3)
            pitchUpdate = "UPDATE pitcher SET Batters_faced = ?, Hits = ?, Opp_avg = ?, Earned_runs = ?, ERA = ? WHERE" \
                          " name = ?"

        if pitchUpdate == "":
            print("Invalid Command")
            return 0

        cur2.execute(pitchUpdate, (newBat, newHitsP, newAvgP, newER, newERA, pitcher,))

        connection.commit()
        cur2.close()
        connection.close()

    # Both AB for the batter, but not a hit. IP for the pitcher is increased by a third, and ERA is updated
    elif result == "FC" or result == "O":

        conn = connect.connectDatabase()
        cur = conn.cursor(buffered=True)
        batQuery = "SELECT At_bat, Hits, RBI FROM batter WHERE name =\'" + batter + "\';"

        cur.execute(batQuery)
        qResult = cur.fetchall()
        for AB, Hits, currRBI in qResult:
            newAB = AB + 1
            newHits = Hits
            newRBI = currRBI + RBI
            newAvg = round(newHits / newAB, 3)

            batUpdate = "UPDATE batter SET At_bat = ?, Hits = ?, Bat_avg = ?, RBI = ? WHERE Name = ?"

        if batUpdate == "":
            print("Invalid query")
            return 0

        cur.execute(batUpdate, (newAB, newHits, newAvg, newRBI, batter))

        conn.commit()
        cur.close()
        conn.close()

        connection = connect.connectDatabase()
        cur2 = connection.cursor(buffered=True)
        pitchQuery = "SELECT Batters_faced, Hits, IP, Earned_runs, ERA FROM pitcher WHERE name = ?"
        cur2.execute(pitchQuery, (pitcher,))
        qResult = cur2.fetchall()
        cur2.close()

        cur2 = connection.cursor()
        for Bat, Hits, IP, currER, ERA in qResult:
            newBat = Bat + 1
            newHitsP = Hits
            # This bit of code increases the Innings pitched to its new value. We cannot just increment by .1, since
            # any value above .2 is invalid. So if the current value is at two thirds innings, we need to change it to
            # the next full inning
            if (IP * 10) % 10 == 2:
                newIP = (IP - .2) + 1
            else:
                newIP = IP + .1
            newER = currER + RBI

            # Inning pitches is weirdly stored as .1 for a third, .2 for two thirds, and .0 for a full inning
            # This bit of code just turns that value into something useful for finding ERA.
            if (newIP * 10 % 10) == 0:
                actualIP = newIP
            elif (((newIP - .1) * 10) % 10) == 0:
                actualIP = (newIP - .1) + .33
            else:
                actualIP = (newIP - .2) + .66

            # ERA is (Earned runs * 9) / Total innings pitched
            newERA = round((newER * 9) / actualIP, 2)
            newAvgP = round(newHitsP / newBat, 3)
            pitchUpdate = "UPDATE pitcher SET Batters_faced = ?, Hits = ?, Opp_avg = ?, Earned_runs = ?, ERA = ? WHERE" \
                          " name = ?"

        if pitchUpdate == "":
            print("Invalid Command")
            return 0

        cur2.execute(pitchUpdate, (newBat, newHitsP, newAvgP, newER, newERA, pitcher,))

        connection.commit()
        cur2.close()
        connection.close()

    elif result == "BB" or result == "HBP":
        conn = connect.connectDatabase()
        cur = conn.cursor(buffered=True)
        batQuery = "SELECT RBI, Walks FROM batter WHERE name =\'" + batter + "\';"

        cur.execute(batQuery)
        qResult = cur.fetchall()
        for currRBI, currBB in qResult:
            newBB = currBB + 1
            newRBI = currRBI + RBI

            batUpdate = "UPDATE batter SET  RBI = ?, Walks = ? WHERE Name = ?"

        if batUpdate == "":
            print("Invalid query")
            return 0

        cur.execute(batUpdate, (newRBI, newBB, batter))

        conn.commit()
        cur.close()
        conn.close()

        connection = connect.connectDatabase()
        cur2 = connection.cursor(buffered=True)
        pitchQuery = "SELECT IP, Earned_runs, ERA FROM pitcher WHERE name = ?"
        cur2.execute(pitchQuery, (pitcher,))
        qResult = cur2.fetchall()
        cur2.close()

        cur2 = connection.cursor()
        for IP, currER, ERA in qResult:

            if (IP * 10) % 10 == 2:
                newIP = (IP - .2) + 1
            else:
                newIP = IP + .1
            newER = currER + RBI

            # Inning pitches is weirdly stored as .1 for a third, .2 for two thirds, and .0 for a full inning
            # This bit of code just turns that value into something useful for finding ERA.
            if (newIP * 10 % 10) == 0:
                actualIP = newIP
            elif (((newIP - .1) * 10) % 10) == 0:
                actualIP = (newIP - .1) + .33
            else:
                actualIP = (newIP - .2) + .66

            # ERA is (Earned runs * 9) / Total innings pitched
            newERA = round((newER * 9) / actualIP, 2)

            pitchUpdate = "UPDATE pitcher SET Earned_runs = ?, ERA = ? WHERE" \
                          " name = ?"

        if pitchUpdate == "":
            print("Invalid Command")
            return 0

        cur2.execute(pitchUpdate, (newER, newERA, pitcher,))

        connection.commit()
        cur2.close()
        connection.close()

    # Strikeout, So batters average decreases, and pitchers strikeout count increases
    elif result == "K":
        conn = connect.connectDatabase()
        cur = conn.cursor(buffered=True)
        batQuery = "SELECT At_bat, Hits FROM batter WHERE name =\'" + batter + "\';"

        cur.execute(batQuery)
        qResult = cur.fetchall()
        for currAB, currHits in qResult:
            newAB = currAB + 1
            newHits = currHits
            newAvg = round(newHits / newAB, 3)

            batUpdate = "UPDATE batter SET At_bat = ?, hits = ?, Bat_avg = ? WHERE Name = ?"

        if batUpdate == "":
            print("Invalid query")
            return 0

        cur.execute(batUpdate, (newAB, newHits, newAvg, batter))

        conn.commit()
        cur.close()
        conn.close()

        connection = connect.connectDatabase()
        cur2 = connection.cursor(buffered=True)

        pitchQuery = "SELECT Batters_faced, Hits, Strikeouts, IP, Earned_runs, ERA FROM pitcher WHERE name = ?"
        cur2.execute(pitchQuery, (pitcher,))
        qResult = cur2.fetchall()
        cur2.close()

        cur2 = connection.cursor()
        for AB, H, K, IP, currER, ERA in qResult:
            newK = K + 1
            newAB = AB + 1
            if (IP * 10) % 10 == 2:
                newIP = (IP - .2) + 1
            else:
                newIP = IP + .1
            newER = currER
            newAvg = round(H / newAB, 3)

            # Inning pitches is weirdly stored as .1 for a third, .2 for two thirds, and .0 for a full inning
            # This bit of code just turns that value into something useful for finding ERA.
            if ((newIP * 10) % 10) == 0:
                actualIP = newIP
            elif ((newIP * 10) % 10) == 1:
                actualIP = (newIP - .1) + .33
            else:
                actualIP = (newIP - .2) + .66

            # ERA is (Earned runs * 9) / Total innings pitched
            newERA = round((newER * 9) / actualIP, 2)

            pitchUpdate = "UPDATE pitcher SET Batters_faced= ?,Strikeouts = ?,Opp_avg = ?, IP = ?, ERA = ? WHERE" \
                          " name = ?"

        if pitchUpdate == "":
            print("Invalid Command")
            return 0

        cur2.execute(pitchUpdate, (newAB, newK, newAvg, newIP, newERA, pitcher,))

        connection.commit()
        cur2.close()
        connection.close()

    # Error results in nothing to be counted for the players involved
    elif result == "E":
        return 0


def divisionQuery(division):
    splitDiv = division.split()
    leagueName = splitDiv[0]
    divName = splitDiv[1]

    teamsQuery = "SELECT division.conf_name, team.Team_name, team.wins, team.loses FROM team INNER JOIN division ON " \
                 "team.dID = division.dID WHERE conf_name = ? AND div_name = ? ORDER BY team.wins DESC;"

    conn = connect.connectDatabase()
    cur = conn.cursor()

    cur.execute(teamsQuery, (leagueName, divName,))

    print("Teams in the " + leagueName + " " + divName + ":")

    for (cName, tName, Wins, Loss) in cur:
        print(tName + " " + str(Wins) + "-" + str(Loss))

    return 0


def leagueQuery(league):
    teamsQuery = "SELECT team.Team_name, team.wins, team.loses FROM team INNER JOIN division ON team.dID = " \
                 "division.dID WHERE conf_name = ? ORDER BY wins DESC;"
    conn = connect.connectDatabase()
    cur = conn.cursor()
    cur.execute(teamsQuery, (league,))

    print("List of all teams in the league")

    for (name, wins, losses) in cur:
        print(name + " " + str(wins) + "-" + str(losses))

    return 0


def mlbQuery():
    teamsQuery = "SELECT Team_name, team.wins, team.loses FROM team ORDER BY wins DESC;"
    conn = connect.connectDatabase()
    cur = conn.cursor()
    cur.execute(teamsQuery)
    print("list of all teams in MLB")

    for (name, wins, losses) in cur:
        print(name + " " + str(wins) + "-" + str(losses))

    return 0


def gameQuery(game):
    splitGame = game.split(',')

    if 4 >= len(splitGame) >= 5:
        print("Invalid command")
        return 0

    # Team names are split into city and name, so we need to split on the whitespace
    winTeam = splitGame[0].strip()
    splitWinTeam = winTeam.split()
    winCity = splitWinTeam[0]
    winName = splitWinTeam[1]

    loseTeam = splitGame[1].strip()
    splitLossTeam = loseTeam.split()
    lossCity = splitLossTeam[0]
    lossName = splitLossTeam[1]

    winPitch = splitGame[2].strip()
    losePitch = splitGame[3].strip()

    if len(splitGame) == 5:
        savePitch = splitGame[4].strip()

    newWins = 0
    newLoss = 0

    # We need many queries in order to update with the needed info
    winQuery = "SELECT Team_name, Wins FROM team WHERE City = ? AND Team_name = ?;"
    conn = connect.connectDatabase()
    cur = conn.cursor()
    cur.execute(winQuery, (winCity, winName,))
    winUpdate = ""

    for (name, wins) in cur:
        newWins = wins + 1
        winUpdate = "UPDATE team SET wins = ? WHERE City = ? AND Team_name = ?;"

    if winUpdate == "":
        print("Invalid Command")
        return 0
    cur.execute(winUpdate, (newWins, winCity, winName,))

    conn.commit()
    cur.close()

    lossQuery = "SELECT Team_name, Loses FROM team WHERE City = ? AND Team_name = ?;"

    cur = conn.cursor()
    cur.execute(lossQuery, (lossCity, lossName,))

    lossUpdate = ""
    for (name, loss) in cur:
        newLoss = loss + 1
        lossUpdate = "UPDATE team SET loses = ? WHERE City = ? AND Team_name = ?;"

    if lossUpdate == "":
        print("Invalid Command")
        return 0

    cur.execute(lossUpdate, (newLoss, lossCity, lossName,))
    conn.commit()
    cur.close()

    winPitchQuery = "SELECT Name, Wins FROM pitcher WHERE Name = ?;"

    cur = conn.cursor()
    cur.execute(winPitchQuery, (winPitch,))

    winPitchUpdate = ""
    for (name, wins) in cur:
        newWins = wins + 1
        winPitchUpdate = "UPDATE pitcher SET Wins = ? WHERE Name = ?;"

    if winPitchUpdate == "":
        print("Invalid Command")
        return 0

    cur.execute(winPitchUpdate, (newWins, winPitch))
    conn.commit()
    cur.close()

    lossPitchQuery = "SELECT Name, Loses FROM pitcher WHERE Name = ?;"

    cur = conn.cursor()
    cur.execute(lossPitchQuery, (losePitch,))

    lossPitchUpdate = ""
    for (name, loss) in cur:
        newLoss = loss + 1
        lossPitchUpdate = "UPDATE pitcher SET Loses = ? WHERE Name = ?;"

    if lossPitchUpdate == "":
        print("Invalid Command")
        return 0

    cur.execute(lossPitchUpdate, (newLoss, losePitch))
    conn.commit()
    cur.close()

    if len(splitGame) == 5:

        saveQuery = "SELECT Name, Saves FROM pitcher WHERE Name = ?;"
        cur = conn.cursor()
        cur.execute(saveQuery, (savePitch,))

        saveUpdate = ""
        for (name, save) in cur:
            newSave = save + 1
            saveUpdate = "UPDATE pitcher SET Saves = ? WHERE Name = ?;"

        if saveUpdate == "":
            print("Invalid Command")
            return 0

        cur.execute(saveUpdate, (newSave, savePitch))
        conn.commit()
        cur.close()

    winManQuery = "SELECT Manager.Name, Manager.Wins FROM manager JOIN team ON manager.tID = team.tID WHERE " \
                  "Team_name = ?;"

    cur = conn.cursor()
    cur.execute(winManQuery, (winName,))

    winManUpdate = ""
    for (name, wins) in cur:
        newWins = wins + 1
        manName = name
        winManUpdate = "UPDATE manager SET wins = ? WHERE Name = ?;"

    if winManUpdate == "":
        print("Invalid Command")
        return 0

    cur.execute(winManUpdate, (newWins, manName,))

    conn.commit()
    cur.close()

    lossManQuery = "SELECT Manager.Name, Manager.Loses FROM manager JOIN team ON manager.tID = team.tID WHERE " \
                   "Team_name = ?;"

    cur = conn.cursor()
    cur.execute(lossManQuery, (lossName,))

    lossManUpdate = ""
    for (name, loss) in cur:
        newLoss = loss + 1
        manName = name
        lossManUpdate = "UPDATE manager SET loses = ? WHERE Name = ?;"

    if lossManUpdate == "":
        print("Invalid Command")
        return 0

    cur.execute(lossManUpdate, (newLoss, manName,))

    conn.commit()
    cur.close()
    conn.close()

    return 0
