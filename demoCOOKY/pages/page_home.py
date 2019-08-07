class PageHome():
    def __init__(self, driver):
        self.driver = driver
        self.home_btn_id = 'action_home'
        self.userinfo_name= 'tvNameUserHome'
#        self.processing_btn_id = 'rbtn_processing'

    def compare_user_info_name(self, name):
        user_name = self.driver.find_element_by_id(self.userinfo_name).text
        assert user_name == name
