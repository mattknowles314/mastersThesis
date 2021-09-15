import json
import matplotlib.pyplot as plt
import os

dataPath="/Volumes/MattData/CricData/odis_json/"

os.chdir(dataPath)
for f in os.listdir():
    with open(dataPath+f,"r") as file:
        data=json.load(file)
        inningsFirst = data["innings"][0]["team"]
        gameDate = data["info"]["dates"]
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
            while i <= len(runsInOvers1)-1:
                RR1.append(sum(runsInOvers1[0:i])/i)
                i+=1
        
            while j <= len(runsInOvers2)-1:
                RR2.append(sum(runsInOvers2[0:j])/j)
                j+=1
            fig, ax = plt.subplots()
            ax.plot(RR1, label="First Innings")
            ax.plot(RR2, label="Second Innings")
            plt.legend(loc="lower right")
            plt.title(graphtitle)
            plt.savefig("/Volumes/MattData/CricData/runrategraphs/"+f.strip(".json")+".png")
        else:
            continue