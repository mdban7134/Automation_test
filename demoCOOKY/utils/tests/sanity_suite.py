from unittest import TestLoader, TestSuite
import HTMLReport  # refer: https://pypi.org/project/HTMLReport/
from demoCOOKY.utils.tests.test_login import TestLogin


class SanitySuite():
    loader = TestLoader()
    suite = TestSuite()

    # add tests to the test suite
    # suite.addTests(loader.loadTestsFromModule(test_login))
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    # runner = HTMLTestRunner(output="../report/")
    runner = HTMLReport.TestRunner(output_path='../report', lang='en', title='Sanity Test Report')
    runner.run(suite)
