import csv
from flask import Flask
import io
import makeGraph as mG
import os
import sys
import base64
from flask import render_template
from helperCheckInput import *

def displayGraph(location, dateRange):
    return getHTML(location, dateRange)

def getData(location, dateRange):
    '''
    get image data from makeGraph
    
    input:  location [county, state]
            dateRange [[Year, Month, Date],[Year, Month, Date]]
    
    output: "Data Not Found!" if no information is found
            image data if the input is correctly formatted and the information is in database
    '''
    output = io.BytesIO()
    
    mG.make2GraphToOutPut(location,dateRange,output)
    
    data = base64.b64encode(output.getvalue()).decode('utf-8 ')
    return data

def getHTML(location, dateRange):
    ''' 
    returns a rendered HTML page according to a location and a dateRange  
    
    input:  location [county, state]
            dateRange [[Year, Month, Date],[Year, Month, Date]]  
    '''
    data = getData(location, dateRange)
    return render_template('graph.html', location = location, dateRange = dateRange,data = data)
