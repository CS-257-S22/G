import datetime
import retrieveData
from indexDictionary import *

dataSet =[]

# TO print the date in which a specific state had the highest reported cases. 
# To do this, we iterate through the data, looking at the reported cases each day for the specified state. 
# We would start with 0, and update a ‘highestDay’ variable if while iterating through there is a day with higher cases than our count.
def getDayWithMostCases(stateName):
    dataSet = retrieveData.retrieveData("Data/dummy_data.csv")
    # first check if stateName is in dataSet
    if stateInData(stateName):
        highestDayCaseCount = 0
        highestDay = "2020-1-1"
        for element in dataSet:
            if (element[stateIndex] == stateName):
                if (int(element[confirmedCaseseIndex]) > int(highestDayCaseCount)):
                    highestDay = element[dateIndex]
                    highestDayCaseCount = element[confirmedCaseseIndex]
        print("On " + dayListToStr(highestDay) +" in " + stateName + " there were " + highestDayCaseCount + " cases." )
        return "On " + dayListToStr(highestDay) +" in " + stateName + " there were " + highestDayCaseCount + " cases."


# Takes list containing date ['year','month','day'] and returns string in form 'Month Day, Year'
def dayListToStr(date): 
    datetime_object = datetime.datetime.strptime(date[1], "%m")
    return datetime_object.strftime("%B") + " " + date[2] + ", " + date[0]

# returns true if state specified is in dataSet, false otherwise
def stateInData(stateName): 
    for element in dataSet:
        if (element[stateIndex] == stateName):
            return True
    print("stateName was not found in dataSet")
    return False