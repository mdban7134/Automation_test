class PageLogin():

    def __init__(self, driver):
        self.driver = driver
        self.loginviaEmail_btn_id = 'rlLoginEmail'
        self.username_txt_id = 'metEmailLogin'
        self.password_txt_id = 'metPassLogin'
        self.login_btn_id = 'tvLogin'
        self.error_message_id = 'md_content'
        self.loginlater_btn_id = 'tvSignInLater'

    def click_loginviaEmail(self):
        self.driver.find_element_by_id(self.loginviaEmail_btn_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_txt_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_txt_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

    def get_error_message_of_login_fail(self):
        return self.driver.find_element_by_id(self.error_message_id).text

    def click_login_later(self):
        self.driver.find_element_by_id(self.loginlater_btn_id).click()
