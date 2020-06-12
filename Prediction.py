from GetDatabaseValues import *
def prediction(team1, team2):
    percentage = [50, 50]
    team1Strength = [getQuaterback(team1),getRunningBacks(team1), getOffensiveLine(team1), getWideRecievers(team1), getRunDefense(team1), getPassDefense(team1)]
    
    f = getStrengthOfTeam(team1Strength)
    
    minorRun1 = team1Strength[1]
    majorRun1 = team1Strength[2]
    avgRun1 = (minorRun1 + majorRun1) /2
    
    minorPass1 = team1Strength[3]
    majorPass1 = team1Strength[0]
    avgPass1 = (minorPass1 + majorPass1) /2
    
    avgQBR1 = (minorPass1 + majorPass1 + majorRun1) /3
    
    runDefense1 = team1Strength[4]
    passDefense1 = team1Strength[5]
    avgDefense1 = (runDefense1 + passDefense1) /2
    #print(f)
    team2Strength = [getQuaterback(team2), getRunningBacks(team2), getOffensiveLine(team2), getWideRecievers(team2), getRunDefense(team2), getPassDefense(team2)]
        
    g = getStrengthOfTeam(team2Strength)
    
    minorRun2 = team2Strength[1]
    majorRun2 = team2Strength[2]
    avgRun2 = (minorRun1 + majorRun2) /2
    
    minorPass2 = team2Strength[3]
    majorPass2 = team2Strength[0]
    avgPass2 = (minorPass2 + majorPass2) /2
    
    avgQBR2 = (minorPass2 + majorPass2 + majorRun2) /3
    
    runDefense2 = team2Strength[4]
    passDefense2 = team2Strength[5]
    avgDefense2 = (runDefense2 + passDefense2) /2
    #print(g)
    percentage = CheckMatchup(f, g, percentage, abs(f-g))
    #RunningBacks vs Run Defense
    percentage = CheckMatchup(minorRun1, runDefense2, percentage, 1)
    percentage = CheckMatchup(runDefense1, minorRun2, percentage, 1)
    #Offensive Line vs Run Defense
    percentage = CheckMatchup(majorRun1, runDefense2, percentage, 2)
    percentage = CheckMatchup(runDefense1, majorRun2, percentage, 2)
    #RunningBacks and Offensive Line vs Run Defense
    percentage = CheckMatchup(avgRun1, runDefense2, percentage, 1.5)
    percentage = CheckMatchup(runDefense1, avgRun2, percentage, 1.5)
    #Wide Recievers vs Pass Defense
    percentage = CheckMatchup(minorPass1, passDefense2, percentage, 1)
    percentage = CheckMatchup(passDefense1, minorPass2, percentage, 1)
    #Quaterbacks vs Pass Defense
    percentage = CheckMatchup(majorPass1, passDefense2, percentage, 1.6)
    percentage = CheckMatchup(passDefense1, majorPass2, percentage, 1.6)
    #Quaterbacks and Wide Recievers vs Pass Defense
    percentage = CheckMatchup(avgPass1, passDefense2, percentage, 1.3)
    percentage = CheckMatchup(passDefense1, avgPass2, percentage, 1.3)
    #Quaterbacks, Wider Recievers, Offensive Line vs Run and Pass Defense
    percentage = CheckMatchup(avgQBR1, avgDefense2, percentage, 2)
    percentage = CheckMatchup(avgDefense1, avgQBR2, percentage, 2)
    for row in percentage:
        print(round(row, 2))
    return percentage


def CheckMatchup(team1, team2, percent, difference):
    if(team1 > team2):
        percent[1] = percent[1] - difference
        percent[0] = percent[0] + difference
    else:
        percent[1] = percent[1] + difference
        percent[0] = percent[0] - difference
    return percent
