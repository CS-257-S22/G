import sys
import makeGraph as mG
import getDayWithMostCases as gDMC
import getTimeData as gTD
import helperCheckInput as hCI
from conversionFunctions import *

state = 0
county = 1
date = 2
graph = 3

help = """Welcome to Coviz, a program that provides informtion and visualization for COVID-19 cases\n
–-state or -s “StateName” returns the latest number of confirmed cases in a given state
–-state or -s “StateName” --county or -c "CountyName" –-daterange or -d “YYYY-MM-DD” “YYYY-MM-DD” returns graphs of the number of cases and deaths in the given county over a time span
"""
def getStateData(stateName):
    gDMC.getDayWithMostCases(stateName)
 
def getDayData(dateRange):
    print(dateRange[0])
    print(dateRange[-1])
    outPut = (gTD.getTimeRange((dateRange[0]), dateRange[-1]))
    if outPut == []:
        return "No Data Found"
    else: return outPut 

def makeGraphOfData(location, dateRange):
    mG.makeGraph(location, dateRange)
    
def CheckComadLine(arguments):
    if (len(arguments) <= 0): return ("No arguments, Try -s or -d")
    elif (len(arguments) == 1):
        return CheckComadLineArg1(arguments)
    elif (len(arguments) == 2) and arguments[1] != "-d":
        return  CheckComadLineArg2(arguments)
    elif (len(arguments) == 3):
        return CheckComadLineArg3(arguments)
    elif (len(arguments) == 5):
        return CheckComadLineArg5(arguments)
    elif (len(arguments) == 7):
        return CheckComadLineArg7(arguments)
    else: return ("Not valid argument, Try: --help")

def setUpValidArguments():
    #create dictonary of commands 
    validArguments = {
        "-s" : state,
        "-–state" : state,
        "-c" : county,
        "--county": county,
        "-d" : date,
        "-–daterange" : date,
        "--help" : help
    }
    return validArguments

def getComadLine():
    #To get valid comand lines converet comand converet sys.argv into string
    arguments = sys.argv[1:]
    return arguments


def compareArgument(argument):
    #check string aganst valid comands 
    validArguments = setUpValidArguments()
    if (argument in (validArguments.keys())):
        return validArguments[argument]
    else: return False
    
def checkValidDate(date):
    #check data in put for valid year month and day 
    date = splitDate(date)
    if (hCI.checkValidDate(date) == False):
        return False
    return date

def CheckComadLineArg1(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == state: return ("Please input state name, Try: -s texas")
    elif compareArgument(str(arguments[0])) == date: return ("Please input date, Try: -d 2020-1-1")
    elif compareArgument(str(arguments[0])) == help: return (help)
    elif compareArgument(str(arguments[0])) == False: return ("Not valid argument, Try: --help")

def CheckComadLineArg2(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == state:
        return getStateData(arguments[1])
    if compareArgument(str(arguments[0])) == date:
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1")
    else: 
        return getDayData(checkValidDate(str(arguments[1])), checkValidDate(str(arguments[1])))

def CheckComadLineArg3(arguments):
    #return correct error 
    if compareArgument(str(arguments[0])) == date: 
        if checkValidDate(str(arguments[1])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        if checkValidDate(str(arguments[2])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([str(arguments[1]),str(arguments[2])])
    else: return ("Not valid argument, Try: --help")

def CheckComadLineArg5(arguments):
    if compareArgument(str(arguments[0])) == state and compareArgument(str(arguments[1])) == date:
        if checkValidDate(str(arguments[3])) == False: return ("Please input valid date, Try: -d 2020-1-1")
        if checkValidDate(str(arguments[4])) == False: return ("Please input valid date, Try: -d 2020-1-1 2020-1-2")
        return getDayData([arguments[2],checkValidDate(str(arguments[3])),checkValidDate(str(arguments[4]))])
    else: return ("Not valid argument, Try: --help")

def CheckComadLineArg7(arguments):
    if (not compareArgument(str(arguments[0])) == state): 
        return ("Invalid input! Try -s Alabama -c Autauga -d 2020-2-1 2020-12-1")
    if (not compareArgument(str(arguments[2])) == county): 
        return ("Invalid input! Try -s Alabama -c Autauga -d 2020-2-1 2020-12-1")
    if (not compareArgument(str(arguments[4])) == date): 
        return ("Invalid input! Try -s Alabama -c Autauga -d 2020-2-1 2020-12-1")
    startDate = checkValidDate(arguments[5])
    endDate = checkValidDate(arguments[6])
    if (startDate == False or endDate == False):
        return ("Please input valid date, Try -s Alabama -c Autauga -d 2020-2-1 2020-12-1")
    location = makeLocation(arguments[3],arguments[1])
    dateRange = makedateRange(arguments[5],arguments[6])
    makeGraphOfData(location, dateRange)
    
if __name__ == '__main__':
    print("""\nNotice: due to the fact that we are operating on a dummy dataset the information may be inaccurate\n""")
    arguments = getComadLine()
    outPut = CheckComadLine(arguments)
    if isinstance(outPut,str):
        print(outPut)
    elif isinstance(outPut,list):
        for row in outPut:
            print(row)

  
