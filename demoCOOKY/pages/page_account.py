class PageAccount():
    def __init__(self, driver):
        self.driver = driver
        self.account_btn_id = 'vn.cooky.cooky:id/action_user'
        self.userprofile_btn_id = 'llSignIn'
        self.cookingclass_btn_id = 'llClass'
        self.draft_btn_id = 'llDraft'
        self.offline_btn_id = 'llOffline'
        self.userrecipecreated_btn_id = 'user_recipe_created'
        self.setting_more_btn_id = 'llSettingMore'
        self.logout_btn_id = 'vn.cooky.cooky:id/llLogOut'
        self.ok_btn_id = 'md_buttonDefaultPositive'
        self.cancel_btn_id = 'md_buttonDefaultNegative'

    def open_tab_account(self):
        self.driver.find_element_by_id(self.account_btn_id).click()

    def click_sign_out(self):
        self.driver.find_element_by_id(self.logout_btn_id).click()

    def click_ok_on_confirmation_popup(self):
        self.driver.find_element_by_id(self.ok_btn_id).click()

    def click_cancel_on_confirmation_popup(self):
        self.driver.find_element_by_id(self.cancel_btn_id).click()

    # def focus_to_button(self):
    #     self.driver.find_element_by_id(self.userrecipecreated_btn_id).focus()
