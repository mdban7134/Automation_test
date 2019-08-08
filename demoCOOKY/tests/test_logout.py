from appium import webdriver
import unittest
import time

# from demoCOOKY.utils import util


from demoCOOKY.pages.page_account import PageAccount
from demoCOOKY.pages.page_intro import PageIntro
from demoCOOKY.pages.page_login import PageLogin
from demoCOOKY.pages.page_home import PageHome


class TestLogout(unittest.TestCase):
    # driver = ''
    def setUp(self):
        appium_url = 'http://localhost:4723/wd/hub'
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0.0',
            'deviceName': '9885f74b4456424952',
            # 'deviceName': 'emulator-5554',
            'app': 'D:/PYTHON/APK/Cooky-3.5.apk',
            'appPackage': 'vn.cooky.cooky',
            'appActivity': 'vn.cooky.cooky.MVP.module.splash_screen.view.SplashScreen'
        }
        self.driver = webdriver.Remote(appium_url, desired_caps)
        self.driver.implicitly_wait(3)

    def test_logout_successful(self):
        page_intro = PageIntro(self.driver)
        page_login = PageLogin(self.driver)
        page_home = PageHome(self.driver)
        page_account = PageAccount(self.driver)
        page_intro.click_next()
        page_intro.click_skip()
        page_login.click_loginviaEmail()
        page_login.enter_username('cooky')
        page_login.enter_password('cooky123123')
        # util.hide_virtual_keyboard(self.driver)
        page_login.click_login()
        #page_login.click_login_later()
        time.sleep(3)
        page_home.click_close_change_log()
        time.sleep(2)
        page_home.open_tab_account()
        start_el = self.driver.find_element_by_id('user_recipe_created')
        end_el = self.driver.find_element_by_id('llSignIn')
        self.driver.scroll(start_el, end_el)
        page_account.click_sign_out()
        page_account.click_ok_on_confirmation_popup()
        time.sleep(3)
        no_signin_message = page_home.validate_login_yet()
        assert no_signin_message == 'Bạn đã có tài khoản để chia sẻ và lưu lại các món ăn chưa?'

    def tearDown(self):
        self.driver.quit()
