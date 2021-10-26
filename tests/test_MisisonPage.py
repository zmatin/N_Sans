from selenium.webdriver import ActionChains
from pageObjects.Homepage import Homepage
from pageObjects.missionPage import MissionPage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):
    def test_two(self):
        misPage = MissionPage(self.driver)
        hmpage = Homepage(self.driver)
        action = ActionChains(self.driver)
        log = self.getlogger()

        aboutTAB = hmpage.getAboutT()
        action.move_to_element(aboutTAB).perform()
        log.info(aboutTAB.is_enabled())

        missionTAB = hmpage.getmissionT()
        log.info(missionTAB.is_enabled())
        action.move_to_element(missionTAB).click().perform()

        self.driver.get_screenshot_as_file("Ourmission.png")
        ourMis = misPage.getmisIMG()
        log.info(ourMis.is_displayed())

        misText = misPage.getMisTXT()
        print(misText)
        log.info("We invite" in misText)





