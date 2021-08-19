import json
import os

def get_dls_results(inputPath, outputPath):
    os.chdir(inputPath)
    for f in os.listdir():
        with open(str(inputPath+f),"r") as read_file:
            data = json.load(read_file)
        if(data["info"]["outcome"]["method"] == "D/L"):
            os.system("mv "+f+" "+outputPath)
