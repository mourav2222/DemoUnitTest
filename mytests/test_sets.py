import unittest
import sys

import allure


sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator
# from parameterized import parameterized, parameterized_class

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("In setupclass() method")
        cls.cal = Calculator(0, 0)

    def test_add1(self):
        self.cal.a = 4
        self.cal.b = -1
        self.assertEqual(self.cal.add(), 3)

    @allure.description("allure: Description 1")
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.step("allure: step1")
    def test_add2(self):
        self.cal.a = -5
        self.cal.b = -1
        self.assertEqual(self.cal.add(), -6)

    @allure.description("allure: Description 2")
    @allure.severity(severity_level=allure.severity_level.NORMAL)
    @allure.step("allure: step2")
    def test_add3(self):
        self.cal.a = 3.2
        self.cal.b = -1.9
        self.assertAlmostEqual(self.cal.add(), 1.3, delta=1)

    def test_add4_2(self):

        assert False
        # try:
        #     assert False
        # finally:
        #     if(AssertionError):
        #         allure.attach(cr)





if __name__ == '__main__':
    unittest.main()
