from selenium.webdriver.common.by import By


class Product_select:
    def __init__(self,driver):
        self.driver = driver
        self.add1 = (By.CSS_SELECTOR,"#main > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(1) > div > div.details > div.add-info > div.buttons > button.button-2.product-box-add-to-cart-button")
        self.add2 = (By.CSS_SELECTOR,"#main > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(4) > div > div.details > div.add-info > div.buttons > button.button-2.product-box-add-to-cart-button")
        self.add3 = (By.CSS_SELECTOR,"#main > div > div.center-2 > div > div.page-body > div.products-container > div.products-wrapper > div > div > div:nth-child(5) > div > div.details > div.add-info > div.buttons > button.button-2.product-box-add-to-cart-button")
        self.cart_click = (By.CSS_SELECTOR,".cart-label")
        
    def product(self):
        self.driver.find_element(*self.add1).click()
        self.driver.find_element(*self.add2).click()
        self.driver.find_element(*self.add3).click()
        self.driver.find_element(*self.cart_click).click()