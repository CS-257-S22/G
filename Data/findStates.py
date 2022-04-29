import sys
import os
sys.path.append("../G")
import retrieveData as rD
dataset = rD.retrieveData("Data/us_simplified.csv")

statenames = []
stateindex = []

stateLocations = []

curStateIndex = 0
curStateName = ""
curCountyName = ""
linenum = -1
newfile = open("stateNameToLineNumber.txt","w")

for line in dataset:
    linenum += 1
    if (not (line[2] == curStateName)):
        curStateName = line[2]
    if (not (line[1] == curCountyName)):
        curCountyName = line[1]
        newfile.write(curCountyName + "," + curStateName + "," + str(linenum) + "\n")  

    
newfile.close()

    