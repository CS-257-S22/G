# 
# This code is not a part of the Command Line project.
# points to improve: 
#   1. low effciency overall; maybe we have to use a smpling method
#   2. the death number is not cumulative, but the confirmed cases seem to be cumulative
import helperMakeGraph as hMG
import matplotlib.pyplot as plt
from helperMakeGraph import *

def makeGraph(location,dateRange):
    """
    Displays 2 graphs according to a location and a date Range

    inputs:
    location (list): [county, state], all elements in String
    dateRange (list): [[Year, Month, Date],[Year, Month, Date]], all elements in String
    """
    info = hMG.getDataForGraph(location,dateRange)
    makeConfirmedCasesGraph(info[0],info[1],location)
    plt.show()
    plt.close()
    makeConfirmedDeathsGraph(info[0],info[2],location)
    plt.show()
    plt.close()

def make2GraphToOutPut(location,dateRange,output):
    '''
    Stores 2 graphs according to a location and a date Range to an output
    
    inputs:
    location (list): [county, state], all elements in String
    dateRange (list): [[Year, Month, Date],[Year, Month, Date]], all elements in String
    output (): a placeholder to save the graph information
    '''
    plt.close()
    plt.rcParams["figure.figsize"] = (15,4)
    
    info = hMG.getDataForGraph(location,dateRange)
    
    plt.subplot(121)
    makeConfirmedCasesGraph(info[0],info[1],location)
    plt.subplot(122)
    makeConfirmedDeathsGraph(info[0],info[2],location)
    plt.tight_layout()
    plt.savefig(output,format="png")
    plt.close()
       
def makeConfirmedCasesGraph(dates, caseList, location):
    '''
    makes a confirmed case graph
    
    inputs:
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    Location is a list of 2, [county, state]
    '''
    
    drawGraph(dates,caseList)
    labelConfirmedCasesToDate()
    makeTitleConfirmedCases(location[0], location[1])
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)

def makeConfirmedDeathsGraph(dates, caseList, location):
    '''
    makes a confirmed deaths graph
    
    inputs:
    dates[] list contains lists of date in the format [Year, Month, Day]
    cases[] list contains number of cases as string
    Location is a list of 2, [county, state]
    '''
    drawGraph(dates,caseList)
    labelConfirmedDeathsToDate()
    makeTitleConfirmedDeaths(location[0], location[1])
    
    timeRangeDays = getTimeRangeDays(dates)
    setXaxisTicks(timeRangeDays)
    
    yticksize = calculateYTickSize(caseList)
    setYaxisTicks(yticksize)
