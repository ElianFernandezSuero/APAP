from selenium import webdriver
from src.pages.nframes_page import nframes_page

def nested_frames_test(driver):
    frames_page = nframes_page(driver)
    frames_page.open()
    frames_page.switch_to_top_frame()
    frames_page.switch_to_left_frame()
    textoIzquierdo = frames_page.get_text_in_left_frame()
    print("Texto del iframe izquierdo: " + textoIzquierdo)

    frames_page.switch_to_default_content()
    frames_page.switch_to_top_frame()
    frames_page.switch_to_right_frame()
    textoDerecho = frames_page.get_text_in_right_frame()
    print("Texto del iframe derecho: " + textoDerecho)

    frames_page.switch_to_default_content()
    frames_page.switch_to_top_frame()
    frames_page.switch_to_middle_frame()
    textoMedio = frames_page.get_text_in_middle_frame()
    print("Texto del iframe medio: " + textoMedio)

    frames_page.switch_to_default_content()
    frames_page.switch_to_second_frame()
    textoBottomFrame = frames_page.get_text_in_second_frame()
    print("Texto del segundo iframe: " + textoBottomFrame)
