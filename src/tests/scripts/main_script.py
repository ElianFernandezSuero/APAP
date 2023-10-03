import unittest
from selenium import webdriver
import unittest
from .test_nframes import nested_frames_test
from .test_tinymce_editor import test_tinymce
from .test_windows import test_windows

class suite(unittest.TestCase):

    def setUp(self):
        self.chrome_driver_path = "C:\\Users\\Elian R. Fernandez\\Desktop\\Practicando Selenium\\Proyectentrevista\\src\\main\\java\\Drivers\\chromedriver2.exe"
        self.driver = webdriver.Chrome()

    def test_tinyMCE(self):
        test_tinymce(self.driver)

    def test_nframes(self):
        nested_frames_test(self.driver)

    def test_windows(self):
        test_windows(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()