from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    loginTab = (By.XPATH, "//a[text()='Log In']")
    lGdisplay = (By.XPATH, "/html/body/div[2]/h3")
    emailUser = (By.XPATH, "//input[@id='username']")
    pasWrd = (By.XPATH, "//input[@id='password']")
    subBut = (By.XPATH, "//input[@id='regularsubmit']")
    aCCdisplay = (By.XPATH, "//div[@class='header-standard']")

    def getloginTab(self):
        return self.driver.find_element(*LoginPage.loginTab).click()

    def getLGdisplay(self):
        return self.driver.find_element(*LoginPage.lGdisplay)

    def getemailUser(self):
        return self.driver.find_element(*LoginPage.emailUser).send_keys("4junkandmore@gmail.com")

    def getPaswrd(self):
        return self.driver.find_element(*LoginPage.pasWrd).send_keys("01Practice!")

    def getSubBut(self):
        return self.driver.find_element(*LoginPage.subBut).click()

    def getAcctDisplay(self):
        return self.driver.find_element(*LoginPage.aCCdisplay)




