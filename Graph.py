# makes a graph out of a dates[] list and a confirmedCases[] list;
# points to improve: the pd.to_datetime() takes a string rather than a list, 
# so the convertDateListtoDateString(dateList) could be saved 
# low effciency overall; maybe we have to use a smpling method
 
import pandas as pd
import ProductionCode as pc
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#dates[] list contains lists of date in the format [Year, Month, Day]
#confirmedCases[] list contains number of cases
def makeConfirmedCasesGraph(dates,confirmedCases):
    
    dates = [pd.to_datetime(convertDateListtoDateString(i)) for i in dates]
    xpoints = dates
    ypoints = confirmedCases
    plt.xlabel("Date")
    plt.ylabel("Confirmed Cases")

    axes = plt.gca()
    # xlocator = matplotlib.ticker.DLocator()
    # axes.xaxis.set_major_locator(xlocator)
    ylocator = matplotlib.ticker.AutoLocator()
    axes.yaxis.set_major_locator(ylocator)

    plt.plot(xpoints, ypoints)
    plt.show()

def convertDateListtoDateString(dateList):
    return dateList[0] + "-" + dateList[1] + "-" + dateList[2]

if __name__ == "__main__":
    pc.relativeDataPath = "Data\plot_test_data.csv"
    pc.retrieveData()
    # makeConfirmedCasesGraph(pc.dataSet[:][0],pc.dataSet[:][3])
    dates = [i[0] for i in pc.dataSet]
    dates.sort
    cases = [i[3] for i in pc.dataSet]
    cases.sort
    makeConfirmedCasesGraph(dates,cases)