from selenium.webdriver.common.by import By

class nframes_page:
    def __init__(self, driver):
        self.top_frame_locator = (By.NAME, "frame-top")
        self.left_frame_locator = (By.NAME, "frame-left")
        self.right_frame_locator = (By.NAME, "frame-right")
        self.middle_frame_locator = (By.NAME, "frame-middle")
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/nested_frames"
        

    def open(self):
        self.driver.get(self.url)
    
    def switch_to_top_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.top_frame_locator))

    def switch_to_left_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.left_frame_locator))

    def get_text_in_left_frame(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_right_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.right_frame_locator))

    def get_text_in_right_frame(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def switch_to_middle_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.middle_frame_locator))

    def get_text_in_middle_frame(self):
        return self.driver.find_element(By.TAG_NAME, "div").text

    def switch_to_second_frame(self):
        self.driver.switch_to.frame(1)

    def get_text_in_second_frame(self):
        return self.driver.find_element(By.TAG_NAME, "body").text
