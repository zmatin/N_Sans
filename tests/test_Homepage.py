from selenium.webdriver import ActionChains
from pageObjects.Homepage import Homepage
from utilities.BaseClass import BaseClass

list1 = []

class TestOne(BaseClass):
    def testone(self):
        hmpage = Homepage(self.driver)
        log = self.getlogger()

        self.driver.get_screenshot_as_file("homepage.png")
        hPimage = hmpage.gethomePIMG()
        log.info(hPimage.is_displayed())

        action = ActionChains(self.driver)
        trainTAB = hmpage.gettrainTab()
        action.move_to_element(trainTAB).perform()
        log.info(trainTAB.is_enabled())

        mangYTTAB = hmpage.getMYTTAB()
        action.move_to_element(mangYTTAB).perform()
        log.info(mangYTTAB.is_enabled())

        rTAB = hmpage.getRTAB()
        action.move_to_element(rTAB).perform()
        log.info(rTAB.is_enabled())

        focusTAB = hmpage.getFocusT()
        action.move_to_element(focusTAB).perform()
        log.info(focusTAB.is_enabled())

        getITAB = hmpage.getInvolve()
        action.move_to_element(getITAB).perform()
        log.info(getITAB.is_enabled())

        aboutTAB = hmpage.getAboutT()
        action.move_to_element(aboutTAB).perform()
        log.info(aboutTAB.is_enabled())
        log.info("all hover buttons verified")

        menuItems = hmpage.getMenuItems()

        for items in menuItems:
            list1.append(items.text)
        log.info(list1)

        cyberTxt = hmpage.getCyberTXT()
        log.info(cyberTxt == hmpage.cybtxt)












