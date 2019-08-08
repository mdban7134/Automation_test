class PageHome():
    def __init__(self, driver):
        self.driver = driver
        self.home_btn_id = 'action_home'
        self.closechangelog_btn_id = 'ivCloseMain'
        self.userinfo_name = 'tvNameUserHome'
        self.nosignin_text = 'tvNoSignIn'
        self.account_btn_id = 'action_user'

    #        self.processing_btn_id = 'rbtn_processing'

    def compare_user_info_name(self, name):
        user_name = self.driver.find_element_by_id(self.userinfo_name).text
        assert user_name == name

    def click_close_change_log(self):
        self.driver.find_element_by_id(self.closechangelog_btn_id).click()

    def open_tab_account(self):
        self.driver.find_element_by_id(self.account_btn_id).click()

    def validate_login_yet(self):
        return self.driver.find_element_by_id(self.nosignin_text).text
