import unittest
import sys
import os

currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)

import ProductionCode as SamProductionCode


class CommandLineTest(unittest.TestCase):
    #Test if the empty comand line response works
    def testComandLineArguments(self):
        #confirms getComadLine is working
        outPut = SamProductionCode.getComadLine();
        self.assertEqual(sys.argv[1:],outPut);
    def testEmptyComandLine(self):
        #checks that the correct error for no arguments is given
        outPut = SamProductionCode.CheckComadLine([]);
        self.assertEqual(outPut,("No arguments, Try -s or -d"));
    def testFalseCompareArgument(self):
        #checks that invalid arguments are false
       self.assertFalse(SamProductionCode.compareArgument(""))
    def testTrueCompareArgument(self):
        #checks that help argument
       self.assertEqual(SamProductionCode.compareArgument("--help"),"""Welcome to Coviz, a program that provides informtion and visualization for COVID-19 cases\n
–-state or -s “StateName” returns the latest number of confirmed cases in a given state
–-state or -s “StateName” --county or -c "CountyName" –-daterange or -d “YYYY-MM-DD” “YYYY-MM-DD” returns graphs of the number of cases and deaths in the given county over a time span
"""        )
       
    def testCheckValidDates(self):
         #checks that valid dates are accepted 
        outPut = SamProductionCode.checkValidDate("2020-1-1")
        self.assertEqual(outPut,["2020","1","1"])
    def testFalseCheckValidDates(self):
         #checks that invalid dates are not accepted 
        outPut = SamProductionCode.checkValidDate("2020-1")
        self.assertFalse(outPut)
    def testArg1(self):
        #checks that errors for comand lines with invalid states are givien 
        outPut = SamProductionCode.CheckComadLineArg1(["-s"]);
        self.assertEqual(outPut,("Please input state name, Try: -s texas"));
    def testFullComandLine(self):
        #checks that errors for comand lines with one invalid date is correctly givien 
       outPut = SamProductionCode.CheckComadLine(["-s","-d","texas","2020-1-1","2002-1-1"]);
       self.assertEqual(outPut,("Please input valid date, Try: -d 2020-1-1 2020-1-2"));


if __name__ == '__main__':
    unittest.main()