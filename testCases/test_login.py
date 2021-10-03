from pageObject.Loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
import os


class TestLoginPage:
    base_url = ReadConfig.base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        logger = LogGen.log_gen()
        if act_title == 'Your store. Login':
            logger.debug("******************** Got the title of the page ********************")
            file_path = os.path.abspath(os.path.dirname(".\\..\screenshots\."))
            self.driver.save_screenshot(file_path + "\Success_Home_page_title.jpg")
            assert True
            self.driver.close()
        else:
            logger.error("******************** Didn't get the title of the page ********************")
            file_path = os.path.abspath(os.path.dirname(".\\..\screenshots\."))
            self.driver.save_screenshot(file_path + "\Error_Home_page_title.jpg")
            self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setup_username(self.username)
        self.lp.setup_password(self.password)
        self.lp.click_login()
        logger = LogGen.log_gen()
        db_title = self.driver.title
        if db_title == "Dashboard / nopCommerce administration":
            logger.debug("******************** Got the title of the page ********************")
            logger.debug("The title for the Dashboard is {}".format(db_title))
            assert True
            file_path = os.path.join('.\\screenshots\\' + 'Dashboard')
            self.driver.save_screenshot(os.path.join(file_path))
            self.driver.close()
        else:
            logger.error("******************** Didn't get the title of the page ********************")
            self.driver.save_screenshot("E:/Videos/Courses/Practice/GIT/automation-framework/screenshots/Dashboard.png")
            self.driver.close()
            assert False
