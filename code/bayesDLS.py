import json
import os
import csv

inputPath = "/Volumes/MattData/CricData/fullFirstInnings/"

#First, we need to filter games for which a full 50 overs were played in first innings
def check_first_innings(inputPath, outputPath):
    os.chdir(inputPath)
    for f in os.listdir():
        with open(inputPath+f,"r") as file:
            data = json.load(file)
            if(len(data["innings"][0]["overs"]) == 50):
                os.system("mv "+f+" "+outputPath)
            else:
                continue

def runsAndWicks(inputPath):
    '''
    Obtains scores from each over and total scores at wicket loss
    '''
    csvF = open("/Volumes/MattData/CricData/firstinns.csv", "a")
    writer = csv.writer(csvF)

    head = ["Game ID"]
    for i in range(0,50):
        head.append(("Over "+str(i+1)))
    for i in range(0,10):
        head.append(("Score at FOW "+str(i+1)))

    writer.writerow(head)

    os.chdir(inputPath)
    for f in os.listdir():
        with open(inputPath+f) as file:
            wickLossScores = []
            gameSum=0
            data = json.load(file)
            row = [f.strip(".json")]
            for o in data["innings"][0]["overs"]:
                overSum=0
                for j in o["deliveries"]:
                    overSum+=j["runs"]["total"]
                    gameSum+=j["runs"]["total"]
                    if "wickets" in j:
                        wickLossScores.append(gameSum)
                row.append(overSum)
            for w in wickLossScores:
                row.append(w)
            writer.writerow(row)


runsAndWicks(inputPath)
