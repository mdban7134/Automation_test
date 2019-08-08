from unittest import TestLoader, TestSuite, TextTestRunner
from HtmlTestRunner import HTMLTestRunner
import HTMLReport  # refer: https://pypi.org/project/HTMLReport/
from demoCOOKY.tests.test_login import TestLogin
from demoCOOKY.tests.test_logout import TestLogout


class SanitySuite():
    loader = TestLoader()
    suite = TestSuite()

    # add tests to the test suite
    # suite.addTests(loader.loadTestsFromModule(test_login))
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestLogout))
    # runner = HTMLTestRunner(output="../report/")
    runner = HTMLReport.TestRunner(output_path='../report', lang='en', title='Sanity Test Report')
    runner.run(suite)
