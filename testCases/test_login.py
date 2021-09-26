import pytest, os
from selenium import webdriver
from pageObject.Loginpage import Login
from main import file_path
import selenium


class TestLoginPage:
    base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setup_username(self.username)
        self.lp.setup_password(self.password)
        self.lp.click_login()
        login_page_title = self.driver.title
        db_title = self.driver.title
        if db_title == "Dashboard / nopCommerce administration":
            print("\nStatus is True")
            assert True
            screenshots = "E:\Framework Project\automation-framework\screenshots"
            self.driver.save_screenshot("screenshots/scrsht.png")
            self.driver.close()

        else:
            assert False

    def test_logout(self, setup):
        self.driver = setup
        self.test_login()
        self.lp = Login()
        self.lp.click_logout()
        self.driver.close()
