class PageLogin():

    def __init__(self, driver):
        self.driver = driver
        self.username_txt_id = 'editTextEmail'
        self.password_txt_id = 'editTextPassword'
        self.login_btn_id = 'btn_login'
        self.error_message_id = 'android:id/message'

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_txt_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_txt_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

    def get_error_message_of_login_fail(self):
        return self.driver.find_element_by_id(self.error_message_id).text