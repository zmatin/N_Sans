from selenium.webdriver import ActionChains

from pageObjects.Homepage import Homepage
from pageObjects.Login import LoginPage
from utilities.BaseClass import BaseClass


class Test_three(BaseClass):
    def test_three(self):
        lGPage = LoginPage(self.driver)
        hmpage = Homepage(self.driver)
        action = ActionChains(self.driver)
        log = self.getlogger()

        lgTab = lGPage.getloginTab()
        if lGPage.getLGdisplay().is_displayed():
            log.info(lGPage.getLGdisplay().is_displayed() == True)

        email = lGPage.getemailUser()
        password = lGPage.getPaswrd()
        signinB = lGPage.getSubBut()
        if lGPage.getAcctDisplay().is_displayed():
            log.info("login successful")
        else:
            log.info("login failed")

        log.info(lGPage.getAcctDisplay().is_displayed() == True)