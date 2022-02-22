import os
import json
from data_handler import *
import csv
import math
path = "C:/Users/iikno/Desktop/DLSGames/"
csvF = open("C:/Users/iikno/Desktop/DLSGames/dlsRR.csv","a")
writer = csv.writer(csvF)
os.chdir(path)
for f in os.listdir():
    with open(path+f,"r") as file:
        data = json.load(file)

        row = [f,data["innings"][1]["target"]["runs"]]

        runsInOvers2 = []

        if len(data["innings"])==2:
            inningsSecond = data["innings"][1]["team"]
            for k in data["innings"][1]["overs"]:
                for p in k["deliveries"]:
                    runsInOvers2.append(p["runs"]["total"])
        
            j=1
            RR2 = []
            
            while j <= len(runsInOvers2):
                row.append(sum(runsInOvers2[0:j])/j)
                j+=1      

            fullOvers = math.floor(j/6)
            print(fullOvers)

            writer.writerow(row)
        else:
            continue

csvF.close()