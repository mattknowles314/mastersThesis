import json
import os
import csv

#Moves all the games from a set of files that were decided by DLS
def get_dls_results(inputPath, outputPath):
    os.chdir(inputPath)
    for f in os.listdir():
        with open(inputPath+f,"r") as file:
            data = json.load(file)
        if("method" in data["info"]["outcome"]):
            if(data["info"]["outcome"]["method"] == "D/L"):
                os.system("move "+f+" "+outputPath)
        

def get_match_data(matchPath, csvPath):
    os.chdir(matchPath)
    for f in os.listdir():
        with open(matchPath+f, "r") as file:
            data = json.load(file)

        homeTeam = data["info"]["teams"][0]
        awayTeam = data["info"]["teams"][1]
        ground = data["info"]["venue"]

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
        
        targetOvers = data["innings"][1]["target"]["overs"]
        targetRuns = data["innings"][1]["target"]["runs"]

        row = homeTeam,awayTeam,ground,winner,str(runsWonBy),str(wicksWonBy),str(targetRuns),str(targetOvers)
        csvF = open(csvPath, "a")
        writer = csv.writer(csvF)
        writer.writerow(row)
        csvF.close()
