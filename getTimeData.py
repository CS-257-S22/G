import retrieveData

dataSet = []
  
# crops dataSet to only consist of data within 2 dates. Both params are inclusive.
def getTimeRange(date1, date2):
    dataSet = retrieveData.retrieveData("Data/dummy_data.csv")
    startDate = dateToList(date1)
    endDate = dateToList(date2)
    returnList = []
    for dataPoint in range(len(dataSet)): 
        currDate = strToIntList(dataSet[dataPoint][0])
        print("currDate = ", currDate)
        print("currDate[0] type ", type(currDate[0]))
        print("startDate[0] type ", type(startDate[0]))
        print("currDate[0] = ", currDate[0], " startDate[0] =", startDate[0])
        if (currDate[0] >= startDate[0] and currDate[0] < endDate[0]):
            print("year check hit")
            if (currDate[1] >= startDate[1] and currDate[1] < endDate[1]):
                print("month check hit")
                if currDate[2] >= startDate[2] and currDate[2] < endDate[2]:
                    print("day check hit")
                    returnList.append(dataSet[dataPoint])                      
    return returnList 

# Converts a "YYYY-MM-DD" string to a list of [year, month, day]        
def dateToList(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:]) 
    return [year, month, day] 

# Converts a list of strings to ints.
def strToIntList(dateList):
    year = int(dateList[0])
    month = int(dateList[1])
    day = int(dateList[2])
    return [year, month, day]       
