from pageObject.Loginpage import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen


class TestLoginPage:
    base_url = ReadConfig.base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            self.logger.info("******************** Got the title of the page ********************")
            assert True
            self.driver.close()
        else:
            self.logger.error("******************** Didn't get the title of the page ********************")
            self.driver.save_screenshot('E:/Videos/Courses/Practice/GIT/automation-framework/screenshots/error.png')
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setup_username(self.username)
        self.lp.setup_password(self.password)
        self.lp.click_login()
        db_title = self.driver.title
        if db_title == "Dashboard / nopCommerce administration":
            self.logger.info("******************** Got the title of the page ********************")
            self.logger.info("The title for the Dashboard is {}".format(db_title))
            assert True
            self.driver.save_screenshot("E:/Videos/Courses/Practice/GIT/automation-framework/screenshots/Dashboard.png")
            self.driver.close()
        else:
            self.logger.error("******************** Didn't get the title of the page ********************")
            self.driver.save_screenshot("E:/Videos/Courses/Practice/GIT/automation-framework/screenshots/Dashboard.png")
            self.driver.close()
            assert False

