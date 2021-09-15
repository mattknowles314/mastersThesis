import json
import matplotlib.pyplot as plt
import os
import csv
dataPath="/Volumes/MattData/CricData/odis_json/"

os.chdir(dataPath)
for f in os.listdir():
    with open(dataPath+f,"r") as file:
        data=json.load(file)
        homeTeam = data["info"]["teams"][0]
        awayTeam = data["info"]["teams"][1]
        ground = data["info"]["venue"]
        inningsFirst = data["innings"][0]["team"]
        gameDate = data["info"]["dates"]

        if "winner" in data["info"]["outcome"]:
            winner = data["info"]["outcome"]["winner"]
            if "runs" in data["info"]["outcome"]["by"]:
                runsWonBy = data["info"]["outcome"]["by"]["runs"]
                wicksWonBy = 0
            else:
                wicksWonBy = data["info"]["outcome"]["by"]["wickets"]
                runsWonBy = 0
        else:
            winner = "tie"

        runsInOvers1 = []
        runsInOvers2 = []
        for i in data["innings"][0]["overs"]:
            for j in i["deliveries"]:
                runsInOvers1.append(j["runs"]["total"])
        if len(data["innings"])==2:
            inningsSecond = data["innings"][1]["team"]
            for k in data["innings"][1]["overs"]:
                for p in k["deliveries"]:
                    runsInOvers2.append(p["runs"]["total"])
        
            graphtitle="Game: ",inningsFirst," vs ",inningsSecond,"; Date: ",gameDate
            i=1
            j=1
            RR1 = []
            RR2 = []
            
            row=[gameDate,homeTeam,awayTeam,winner,runsWonBy,wicksWonBy]
            
            while i <= len(runsInOvers1)-1:
                row.append(sum(runsInOvers1[0:i])/i)
                i+=1
            row.append("EOI")
            while j <= len(runsInOvers2)-1:
                row.append(sum(runsInOvers2[0:j])/j)
                j+=1       

            csvF = open("/Volumes/MattData/CricData/rrmaster.csv", "a")
            writer = csv.writer(csvF)
            writer.writerow(row)
            csvF.close()
        else:
            continue