import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Filter_laptop_price(unittest.TestCase):
    LAPTOP_CATEGORY = (By.XPATH, '//a[@class="parentCategName"]')
    LAPTOP_CATEGORY_2 = (By.CSS_SELECTOR, 'a.category[href="https://www.cel.ro/laptop-laptopuri/"]')
    SORT_LAPTOPS = (By.ID, "sortare")
    SORT_LAPTOPS_BY_PRICE = (By.XPATH, '//*[@id="sortare"]/option[3]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://www.cel.ro")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_filter_laptop_price(self):
        self.chrome.find_element(*self.LAPTOP_CATEGORY).click()
        self.chrome.find_element(*self.LAPTOP_CATEGORY_2).click()
        self.chrome.find_element(*self.SORT_LAPTOPS).click()
        self.chrome.find_element(*self.SORT_LAPTOPS_BY_PRICE).click()

