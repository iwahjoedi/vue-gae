import unittest
from usertest import UserTestCase

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(UserTestCase ))
    return test_suite
    
mySuit=suite()

runner=unittest.TextTestRunner()
runner.run(mySuit)