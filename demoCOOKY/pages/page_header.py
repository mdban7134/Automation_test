class PageHeader():
    def __init__(self, driver):
        self.driver = driver
        self.freepick_btn_id = 'rbtn_order_pick'
        self.processing_btn_id = 'rbtn_processing'

    def compare_freepick_button_name(self, name):
        freepick_text = self.driver.find_element_by_id(self.freepick_btn_id).text
        assert freepick_text == name
