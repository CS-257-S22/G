import sys
import os
sys.path.append("../G")
import retrieveData as rD


with open("Data/us_simplified.csv") as file:
    originalData = file.readlines()
originalData = originalData[1:]

with open("Data/stateNameToLineNumber.txt") as index:
    lines = index.readlines()

locations = []
indexs = []
for i in lines:
    v3 = i.split(",")
    locations.append(v3[0] + "," + v3[1])
    indexs.append(int(v3[2]))

tmp = 0
for location in locations:
    filename = location+".csv"
    path = "Data/sub-Data/" + filename
    newfile = open(path,"w")
    newfile.write("Date,Admin2,Province/State,Confirmed,Deaths,Country/Region\n")
    thisindex = indexs[tmp]
    nextindex = 0
    if(tmp == len(indexs) -1): nextindex = len(originalData)
    else: nextindex = indexs[tmp+1]
    for i in range(thisindex, nextindex):
        newfile.write(originalData[i])
    newfile.close()
    tmp += 1