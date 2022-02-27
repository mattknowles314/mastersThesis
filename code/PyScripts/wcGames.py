import os
import json
from data_handler import *
import csv
import math
csvF = open("C:/Users/iikno/Desktop/DLSGames/dlsRR.csv","a")
writer = csv.writer(csvF)

def remove_non_odis(path):
    os.chdir(path)
    delList = []
    for f in os.listdir():
        with open(path+f,"r") as file:
            data = json.load(file)
            if data["info"]["match_type"] != "ODI":
                delF = 1
            else:
                continue
        if delF == 1:
            delList.append(f)
    
    for i in delList:
        os.remove(path+i)

def remove_non_years(path, year):
    os.chdir(path)
    delList = []
    for f in os.listdir():
        with open(path+f,"r") as file:
            data = json.load(file)
            if not (str(year) in data["info"]["dates"][0]):
                delF = 1
            else:
                continue
        if delF == 1:
            delList.append(f)
    for i in delList:
        os.remove(path+i)


def remove_non_wc(path):
    os.chdir(path)
    delList = []
    for f in os.listdir():
        with open(path+f,"r") as file:
            data = json.load(file)
            if data["info"]["event"]["name"] != "World Cup":
                delF = 1
            else:
                continue
        if delF == 1:
            delList.append(f)
    for i in delList:
        os.remove(path+i)        

afgPath = "C:/Users/iikno/Desktop/afghanistan_male_json/" #216
pakPath = "C:/Users/iikno/Desktop/pakistan_male_json/" #646

#remove_non_odis(afgPath)
#remove_non_odis(pakPath)
#remove_non_years(afgPath,2019) #20
#remove_non_years(pakPath,2019) #25
remove_non_wc(afgPath)
remove_non_wc(pakPath)