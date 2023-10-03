from selenium import webdriver
from src.pages.tinymce_editor_page import TinyMCEPage
import time

def test_tinymce(driver):
    tinyMCE = TinyMCEPage(driver)
    tinyMCE.open()
    tinyMCE.switch_to_iframe()
    tinyMCE.clear_and_type_text("Hola")
    tinyMCE.select_all_text()
    tinyMCE.apply_bold_formatting()
    tinyMCE.switch_to_default_content()
    tinyMCE.apply_text_color("Red")
    tinyMCE.apply_text_alignment("Align center")
    saved_text = tinyMCE.get_saved_text()
    time.sleep(5)
    print("Texto Guardado: " + saved_text)
