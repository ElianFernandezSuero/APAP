from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TinyMCEPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/tinymce")

    def switch_to_iframe(self):
        iframe = self.driver.find_element(By.ID, "mce_0_ifr")
        self.driver.switch_to.frame(iframe)

    def clear_and_type_text(self, text):
        iframe_textbox = self.driver.find_element(By.ID, "tinymce")
        iframe_textbox.clear()
        iframe_textbox.send_keys(text)

    def select_all_text(self):
        iframe_textbox = self.driver.find_element(By.ID, "tinymce")
        iframe_textbox.send_keys(Keys.CONTROL + "a")

    def apply_bold_formatting(self):
        iframe_textbox = self.driver.find_element(By.ID, "tinymce")
        iframe_textbox.send_keys(Keys.CONTROL + "b")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def apply_text_color(self, color_name):
        elemento_menubar = self.driver.find_element(By.CSS_SELECTOR, "#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-menubar > button:nth-child(4)")
        elemento_menubar.click()
        time.sleep(1)
        TextColor = self.driver.find_element(By.XPATH, "//div[@title='Text color']")
        TextColor.click()
        color_element = self.driver.find_element(By.XPATH, f"//div[@title='{color_name}']")
        color_element.click()

    def apply_text_alignment(self, alignment_name):
        alignment_button = self.driver.find_element(By.CSS_SELECTOR, f"button[title='{alignment_name}']")
        alignment_button.click()

    def get_saved_text(self):
        self.switch_to_iframe()
        textoGuardado = self.driver.find_element(By.ID, "tinymce").text
        self.switch_to_default_content()
        return textoGuardado

    def close(self):
        self.driver.quit()