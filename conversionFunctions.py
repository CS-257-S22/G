from datetime import datetime
def toDateTime(date):
    '''convert date [Year, Month, Day] to a datetime object'''
    return datetime(int(date[0]),int(date[1]),int(date[2]))

def splitDate(dateString):
    '''Split date in to a list [Year, Month, Day]'''
    dates = dateString.split("-")
    return dates

def makedateRange(startDateString,endDateString):
    '''
    converts Strings of startDateString and endDateString (both formatted "YYYY-MM-DD")
    to a dateRange list [startDateList,endDateList] ([[Year, Month, Day],[Year, Month, Day]])
    '''
    dateRange = [splitDate(startDateString),splitDate(endDateString)]
    return dateRange

def makeLocation(county,state):
    '''
    converts two String variables, county and state into a list [county,state]
    '''
    return [county,state]