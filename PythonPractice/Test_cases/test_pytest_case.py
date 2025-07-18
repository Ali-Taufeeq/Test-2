import pytest
from selenium import webdriver
from urllib3 import request

from Page_objects.Product_selection import Product_select
from Page_objects.get_url import URL_LOGIN
from Page_objects.hover import Hover
from Page_objects.total import Total_validation
from Test_cases.conftest import browser


@pytest.mark.usefixtures("browser")
class Testlogin:
    def test_Login(self):
        login_test = URL_LOGIN(self.driver)
        login_test.Login()

@pytest.mark.usefixtures("browser")
class Test_Options:
    def test_cell(self):
        cell_phone = Hover(self.driver)
        cell_phone.hover_click()

@pytest.mark.usefixtures("browser")
class Test_Product_select:
    def test_product(self):
        p_select = Product_select(self.driver)
        p_select.product()

@pytest.mark.usefixtures("browser")
class Test_Total_price:
    def test_price(self):
        correct_price = Total_validation(self.driver)
        correct_price.sum_validate()

