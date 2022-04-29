import unittest
import getTimeData
import retrieveData

testData = retrieveData.retrieveData("Data/dummy_data.csv")

class TestSum(unittest.TestCase):
    def testDateToList(self):
        newList = getTimeData.dateToList("2020-15-22")
        correctList = [2020, 15, 22]
        self.assertEqual(newList, correctList)

    def testStrToIntList(self):
        newList = getTimeData.strToIntList(["2020", "15", "22"])
        correctList = [2020, 15, 22]
        self.assertEqual(newList, correctList)
    
    def testGetTimeRange(self):
        testCorrect = []
        for groupIndex in testData:
            print("groupIndex = ", groupIndex)
            if groupIndex == 11 or groupIndex == 20 or groupIndex == 74:
                print("if hit with group index ", groupIndex)
                testCorrect.append(testData[groupIndex])
        testSet = testData 
        newSet = getTimeData.getTimeRange("2021-02-17", "2021-02-20") 
        self.assertEqual(newSet, testCorrect) 

    

if __name__ == '__main__':
    unittest.main()
