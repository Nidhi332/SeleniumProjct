from selenium import webdriver
from Guru99_Bank import ConstantUtil
import unittest
from Guru99_Bank.com.guru.pages import LoginPage

class verifyLogin(unittest.TestCase):
    driver=webdriver.Firefox(executable_path=ConstantUtil.DRIVER_PATH)
    driver.get(ConstantUtil.URL)
    driver.maximize_window()


    def test_login(self):
        loginPage=LoginPage(self.driver)
        loginPage.getUserNameElement().send_keys("mngr254117")
        loginPage.getPasswordElement().send_keys("zAvYtAv")
        loginPage.getLoginButton().click()

    driver.quit()