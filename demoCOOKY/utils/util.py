from appium import webdriver


def accept_permission(driver):
    permission_allow_btn_id = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
    permission_allow_btn_id.click()


def hide_virtual_keyboard(driver):
    driver.hide_keyboard()


def hide_virtual_keyboar():
    return None


