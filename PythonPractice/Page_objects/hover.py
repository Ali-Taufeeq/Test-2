import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Test_cases.conftest import browser


@pytest.mark.usefixtures("browser")
class Hover:
    def __init__(self,driver):
        self.driver = driver
        self.hover = (By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[2]/a")
        self.cell_phone = (By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']")

    def hover_click(self):
        just_hover = self.driver.find_element(*self.hover)
        action = ActionChains(self.driver)
        action.move_to_element(just_hover).perform()
        self.driver.find_element(*self.cell_phone).click()
        time.sleep(5)
