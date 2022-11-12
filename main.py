import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_calculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_calc_percentage(self):
        driver = self.driver

        driver.get("http://www.calculator.net/")

        # Comprobar title
        title = driver.title
        self.assertIn("Calculator.net: Free Online Calculators - Math, Fitness, Finance, Science", driver.title)

        # implicit wait
        driver.implicitly_wait(10)

        # Maximize the browser
        driver.maximize_window()

        # Click on Math Calculators
        math_calc = driver.find_element(by=By.XPATH, value="//div[@id='contentout']/table/tbody/tr/td[3]/div[@class='hh']")
        math_calc.click()

        driver.implicitly_wait(10)

        # Click on Percent Calculators
        perc_calc = driver.find_element(by=By.XPATH, value="//table[@class='smtb'][1]/tbody/tr/td/div[3]/a")
        perc_calc.click()

        # Enter value 10 in the first number of the percent Calculator
        first_num = driver.find_element(by=By.ID, value="cpar1")
        first_num.send_keys(10)

        # Enter value 50 in the second number of the percent Calculator
        second_num = driver.find_element(by=By.ID, value="cpar2")
        second_num.send_keys(50)

        #Click Calculate Button
        button = driver.find_element(by=By.XPATH, value=".//*[@value = 'Calculate']")
        button.click()

        #Get the Result Text based on its xpath
        result = driver.find_element(by=By.CLASS_NAME, value="h2result").text
        self.assertIn("Result: 5", result)
        driver.implicitly_wait(10)

        #Print a Log In message to the screen
        print(f"\nResult = {result}")

    def tearDown(self):
        # Close the Browser.
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

