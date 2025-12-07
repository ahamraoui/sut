from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoutiquePage:
    def __init__(self, driver):
        self.driver = driver
    def search_article(self, code_or_keyword):
        search_box = self.driver.find_element(By.ID, "search-bar")
        search_box.clear()
        search_box.send_keys(code_or_keyword)
        self.driver.find_element(By.ID, "search-btn").click()
    def get_articles(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "article-item"))
        )
    def add_article_to_cart(self):
        plus_one_btn = self.driver.find_element(By.CSS_SELECTOR, ".plus-one.active")
        plus_one_btn.click()
    def add_unavailable_article(self):
        plus_one_btn = self.driver.find_element(By.CSS_SELECTOR, ".plus-one.inactive")
        plus_one_btn.click()
    def get_unavailable_btn_color(self):
        plus_one_btn = self.driver.find_element(By.CSS_SELECTOR, ".plus-one.inactive")
        return plus_one_btn.value_of_css_property("color")
    def get_cart_count(self):
        return int(self.driver.find_element(By.ID, "panier-count").text)

