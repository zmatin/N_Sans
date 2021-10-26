from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    homepIMG = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/picture/img")
    trainT = (By.XPATH, "//*[@id='__layout']/div/header/div/div/div/div/nav[1]/ul/li[1]/a")
    mYTTAB = (By.XPATH, "//*[@id='__layout']/div/header/div/div/div/div/nav[1]/ul/li[2]/a")
    resourceT = (By.XPATH, "//*[@id='__layout']/div/header/div/div/div/div/nav[1]/ul/li[3]/a")
    focusT = (By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div/nav[1]/ul/li[4]/a")
    getinvlv = (By.XPATH, "//*[@id='__layout']/div/header/div/div/div/div/nav[1]/ul/li[5]/a")
    aboutT = (By.XPATH, "//*[@id='__layout']/div/header/div/div/div/div/nav[1]/ul/li[6]/a")
    missionT = (By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div/nav[1]/ul/li[6]/ul/li[3]/a")
    cyberText = (By.XPATH, "//h1[@class='image-banner__title own-styles']")
    cybtxt = "Cyber Security Training, Certifications, Degrees and Resources"
    menuitems = (By.XPATH, "//li[@role='menuitem']")



    def gethomePIMG(self):
        return self.driver.find_element(*Homepage.homepIMG)

    def gettrainTab(self):
        return self.driver.find_element(*Homepage.trainT)

    def getMYTTAB(self):
        return self.driver.find_element(*Homepage.mYTTAB)

    def getRTAB(self):
        return self.driver.find_element(*Homepage.resourceT)

    def getFocusT(self):
        return self.driver.find_element(*Homepage.focusT)

    def getInvolve(self):
        return self.driver.find_element(*Homepage.getinvlv)

    def getAboutT(self):
        return self.driver.find_element(*Homepage.aboutT)

    def getmissionT(self):
        return self.driver.find_element(*Homepage.missionT)

    def getCyberTXT(self):
        return self.driver.find_element(*Homepage.cyberText).text

    def getMenuItems(self):
        return self.driver.find_elements(*Homepage.menuitems)




