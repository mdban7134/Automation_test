from appium import webdriver
import unittest
import time

# from demoCOOKY.utils import util
from demoCOOKY.pages.page_account import PageAccount
from demoCOOKY.pages.page_intro import PageIntro
from demoCOOKY.pages.page_login import PageLogin
from demoCOOKY.pages.page_home import PageHome


class TestLogin(unittest.TestCase):
    # driver = ''
    def setUp(self):
        appium_url = 'http://localhost:4723/wd/hub'
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            # 'deviceName': '9885f74b4456424952',
            'deviceName': 'emulator-5554',
            'app': 'D:/PYTHON/APK/Cooky-3.5.apk',
            'appPackage': 'vn.cooky.cooky',
            'appActivity': 'vn.cooky.cooky.MVP.module.splash_screen.view.SplashScreen'
        }
        self.driver = webdriver.Remote(appium_url, desired_caps)
        self.driver.implicitly_wait(3)
        # permission_allow_btn_id = self.driver.find_element_by_id(
        #     'com.android.packageinstaller:id/permission_allow_button')
        # while True:
        #     try:
        #         permission_allow_btn_id.click()
        #     except:
        #         break

    # def test_logout_successful(self):
    #     page_intro = PageIntro(self.driver)
    #     page_login = PageLogin(self.driver)
    #     page_home = PageHome(self.driver)
    #     page_account = PageAccount(self.driver)
    #     page_intro.click_next()
    #     page_intro.click_skip()
    #     page_login.click_loginviaEmail()
    #     page_login.enter_username('cooky')
    #     page_login.enter_password('cooky123123')
    #     # util.hide_virtual_keyboard(self.driver)
    #     page_login.click_login()
    #     time.sleep(3)
    #     page_home.click_close_change_log()
    #     page_account.open_tab_account()
    #     page_account.click_sign_out()
    #     page_account.click_ok_on_confirmation_popup()

    def test_login_successful(self):
        page_intro = PageIntro(self.driver)
        page_login = PageLogin(self.driver)
        page_intro.click_next()
        page_intro.click_skip()
        page_login.click_loginviaEmail()
        page_login.enter_username('cooky')
        page_login.enter_password('cooky123123')
        # util.hide_virtual_keyboard(self.driver)
        page_login.click_login()

        time.sleep(3)

        page_home = PageHome(self.driver)
        page_home.compare_user_info_name('Cooky VN')

    def test_login_fail_with_invalid_password(self):
        page_intro = PageIntro(self.driver)
        page_login = PageLogin(self.driver)
        page_intro.click_next()
        page_intro.click_skip()
        page_login.click_loginviaEmail()
        page_login.enter_username('tien.testlogin123')
        page_login.enter_password('111111')
        # util.hide_virtual_keyboar(self.driver)
        page_login.click_login()

        time.sleep(3)
        error_message = page_login.get_error_message_of_login_fail()
        assert error_message == 'Email hoặc password không đúng'

    def tearDown(self):
        self.driver.quit()
