from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class URL_LOGIN:
    def __init__(self,driver):
        self.driver = driver
        self.click_login = (By.CSS_SELECTOR,".ico-login")
        self.email = (By.CSS_SELECTOR,".email")
        self.user_name = "er.taufeeqali@gmail.com"
        self.pwd = (By.CSS_SELECTOR,".password")
        self.password = 123456
        self.remember = (By.NAME,"RememberMe")
        self.login_btn = (By.CSS_SELECTOR,".login-button")

    def Login(self):

        self.driver.find_element(*self.click_login).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(*self.email))
        self.driver.find_element(*self.email).send_keys(self.user_name)
        self.driver.find_element(*self.pwd).send_keys(self.password)
        self.driver.find_element(*self.remember).click()
        self.driver.find_element(*self.login_btn).click()





