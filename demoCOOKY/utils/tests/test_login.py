from appium import webdriver
import unittest
import time
from demoCOOKY.utils import util
from demoCOOKY.pages.page_login import PageLogin
from demoCOOKY.pages.page_header import PageHeader


class TestLogin(unittest.TestCase):
    # driver = ''
    def setUp(self):
        appium_url = 'http://localhost:4723/wd/hub'
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': '8cd39035',
            'app': 'D:/PythonCode/python_qa/demoCOOKY/apk/app-vn-debug-9.17-v224.apk',
            'appPackage': 'vn.foody.delivery.debug',
            'appActivity': 'com.foody.delivery.presentation.ui.splash.FdSplashActivity_'
        }
        self.driver = webdriver.Remote(appium_url, desired_caps)
        self.driver.implicitly_wait(3)
        permission_allow_btn_id = self.driver.find_element_by_id(
            'com.android.packageinstaller:id/permission_allow_button')
        while True:
            try:
                permission_allow_btn_id.click()
            except:
                break

    def test_login_successful(self):
        page_login = PageLogin(self.driver)
        page_login.enter_username('trung.shipper100')
        page_login.enter_password('123456')
        util.hide_virtual_keyboar(self.driver)
        page_login.click_login()

        time.sleep(3)

        page_header = PageHeader(self.driver)
        page_header.compare_freepick_button_name('FREE-PICK')

    def test_login_fail_with_invalid_password(self):
        page_login = PageLogin(self.driver)
        page_login.enter_username('trung.shipper100')
        page_login.enter_password('111111')
        util.hide_virtual_keyboar(self.driver)
        page_login.click_login()

        time.sleep(3)
        error_message = page_login.get_error_message_of_login_fail()
        assert error_message == 'Tên đăng nhập hoặc mật khẩu không chính xác'

    def tearDown(self):
        self.driver.quit()
