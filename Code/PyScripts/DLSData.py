import os
import json
from data_handler import *
import csv
import math
path = "C:/Users/iikno/Desktop/wcDls/"
csvF = open("C:/Users/iikno/Desktop/wcdlsRR.csv","a")
writer = csv.writer(csvF)
os.chdir(path)
for f in os.listdir():
    with open(path+f,"r") as file:
        data = json.load(file)

        row = [f,data["innings"][0]["team"]]
        runsInOvers2 = []

        if len(data["innings"])==2:
            for k in data["innings"][0]["overs"]:
                overSum = 0
                for p in k["deliveries"]:
                    overSum += p["runs"]["total"]
                runsInOvers2.append(overSum)
        
            j=1
            RR2 = [runsInOvers2[0]]
            while j <= len(runsInOvers2):
                RR2.append(sum(runsInOvers2[0:j])/j)
                j+=1
            
            for i in RR2:
                row.append(i)
            writer.writerow(row)
        else:
            continue

csvF.close()