# Generate a small dummy dataset to work with
import csv
import random
with open("us_simplified.csv") as file:
    lines = file.readlines()
numlines = len(lines)

randList = random.sample(range(1,numlines), 200)
newfile = open("dummy_data.csv","w")
newfile.write(lines[0])
for i in randList:
    newfile.write(lines[i])
file.close()
newfile.close()