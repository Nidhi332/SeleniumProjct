class LoginPage:
    textbox_username_xpath ="/html/body/form/table/tbody/tr[1]/td[2]/input"
    textbox_password_name = "password"
    button_login_name = "btnLogin"

    def __init__(self,driver):
        self.driver=driver

    def getUserNameElement(self):
        return self.driver.find_element_by_xpath(self.textbox_username_xpath)

    def getPasswordElement(self):
        return self.driver.find_element_by_name(self.textbox_password_name)

    def getLoginButton(self):
        return self.driver.find_element_by_name(self.button_login_xpath)
