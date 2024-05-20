import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver_path = '/mnt/c/path/to/chromedriver'  # Update this path accordingly
        service = ChromeService(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:5000/login")

    def test_login(self):
        driver = self.driver
        # Locate username field
        username_field = driver.find_element(By.NAME, 'Username:')
        # Locate password field
        password_field = driver.find_element(By.NAME, 'Password:')
        # Locate login button
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

        # Enter credentials
        username_field.send_keys('imrea1m')
        password_field.send_keys('HelloWorld12345')  # Assuming 'password' is the correct password
        login_button.click()

        # Wait for a few seconds to see the results
        time.sleep(5)

        # Check if login was successful by checking a page element
        welcome_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome')]")
        self.assertIsNotNone(welcome_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()