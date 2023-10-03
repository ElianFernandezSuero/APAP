from selenium import webdriver
import sys
from src.pages.windows_page import WindowsPage
import time

def test_windows(driver):
    windows = WindowsPage(driver)
    windows.open()
    original_window_handle = windows.get_current_window_handle()
    windows.click_on_click_here_link()
    new_window_handle = windows.switch_to_new_window(original_window_handle)
    text_in_new_window = windows.get_text_in_new_window()
    print("Texto en la nueva ventana: " + text_in_new_window)
    windows.close_new_window()
    windows.switch_to_original_window(original_window_handle)
    time.sleep(5)
    windows.close()
