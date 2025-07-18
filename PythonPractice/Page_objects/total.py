import time
from functools import total_ordering
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Total_validation:
    def __init__(self,driver):
        self.driver = driver
        self.P1 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[3]/div[2]/button[1]")
        self.P2 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[4]/div/div[2]/div[3]/div[2]/button[1]")
        self.P3 = (By.XPATH,"//*[@id='main']/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[5]/div/div[2]/div[3]/div[2]/button[1]")
        self.total = (By.CSS_SELECTOR,"#shopping-cart-form > div.cart-footer > div.totals > div.total-info > table > tbody > tr.order-total > td.cart-total-right > span > strong")

    def clean_price(self,price_str):
        return float(price_str.replace("$","").replace(",","").strip())

    def sum_validate(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.P1)
        )
        add_p1 = self.clean_price(self.driver.find_element(*self.P1).text)
        add_p2 = self.clean_price(self.driver.find_element(*self.P2).text)
        add_p3 = self.clean_price(self.driver.find_element(*self.P3).text)
        price = self.clean_price(self.driver.find_element(*self.total).text)

        sum = add_p1 + add_p2 + add_p3
        if sum != price:
            raise Exception("Price is incorrect")
