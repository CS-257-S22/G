import helperCheckInput as hCI
import conversionFunctions as cF
InvalidCountyStateMsg = "This county-state pair does not exist! Check spelling."

def checkFlaskInput(countyName, stateName, startDate, endDate): # !!! need to know what type the inputs will be
    '''
    checks if all the input is correct
    input:  countyName in String
            stateName in String
            startDate in String
            endDate in String
    return: True if all the input are correct
            Error message(s) if not
    '''
    checkcountyStateResult = checkCountyState(countyName, stateName)
    checkDateResult = checkDate(startDate, endDate)
    checkInputResult = ""
    if (checkcountyStateResult != True):
        checkInputResult += checkcountyStateResult
        checkInputResult += "<br/>"
    if (checkDateResult != True):
        checkInputResult += checkDateResult
        checkInputResult += "<br/>"
    if (checkInputResult == ""):
        return True
    return checkInputResult


def checkCountyState(countyName,stateName):
    '''
    Check if dates are within range and ordered correctly.
    Returns True if no error, or an error msg.
    '''
    stateCountyData = open('Data/stateNameToLineNumber.txt','r')
    for line in stateCountyData:
        dataList = line.split(",")
        if (countyName == dataList[0] and stateName == dataList[1]):
            stateCountyData.close()
            return True
    stateCountyData.close()
    return InvalidCountyStateMsg


def checkDate(start, end):
    '''
    Check if dates are within range and ordered correctly.
    Returns True if no error, or an error msg.
    '''
    return hCI.checkDates(cF.splitDate(start), cF.splitDate(end)) 