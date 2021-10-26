from selenium.webdriver.common.by import By


class MissionPage:
    def __init__(self, driver):
        self.driver = driver

    misIMG = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/picture/img")
    misTXT = (By.XPATH, "//*[@id='__layout']/div/div/div/div/div/div/div/div/div")


    def getmisIMG(self):
        return self.driver.find_element(*MissionPage.misIMG)

    def getMisTXT(self):
        return self.driver.find_element(*MissionPage.misTXT).text





