import unittest
import sys
import os
#access mother directory
currentPath = os.path.dirname(__file__)
motherdir = os.path.join(currentPath,"..")
sys.path.append(motherdir)
from FlaskApp import *

class flaskTestGraph(unittest.TestCase):

    #the graphs cannot be unit-checked, so all tests are integral
    
    def testPageNotFound(self):
        '''tests invalid page'''
        self.app = app.test_client()
        response = self.app.get('/.....', follow_redirects=True)
        response = str(response.data)
        isCorrect = ("We are sorry but we could not find the page you are looking for" in response)
        self.assertTrue(isCorrect)
    
        
if __name__ == '__main__':
    unittest.main()
   
