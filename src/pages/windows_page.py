from selenium.webdriver.common.by import By
import time

class WindowsPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def click_on_click_here_link(self):
        click_here_link = self.driver.find_element(By.LINK_TEXT, "Click Here")
        click_here_link.click()

    def switch_to_new_window(self, original_window_handle):
        ventanas_abiertas = self.driver.window_handles
        for ventana in ventanas_abiertas:
            if ventana != original_window_handle:
                self.driver.switch_to.window(ventana)
                return ventana

    def get_text_in_new_window(self):
        texto_nueva_ventana = self.driver.find_element(By.TAG_NAME, "h3").text
        return texto_nueva_ventana

    def close_new_window(self):
        self.driver.close()

    def switch_to_original_window(self, original_window_handle):
        self.driver.switch_to.window(original_window_handle)

    def close(self):
        self.driver.quit()
