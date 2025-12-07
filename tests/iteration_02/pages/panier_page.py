from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PanierPage:
    def __init__(self, driver):
        self.driver = driver
    def get_articles(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "panier-article"))
        )
    def remove_article(self):
        moins_un_btn = self.driver.find_element(By.CSS_SELECTOR, ".moins-un")
        moins_un_btn.click()
    def confirm_removal(self):
        confirm_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "confirm-suppression"))
        )
        confirm_btn.click()
    def get_empty_message(self):
        try:
            return self.driver.find_element(By.ID, "panier-vide-message").text
        except:
            return None
    def confirm_cart(self):
        self.driver.find_element(By.ID, "confirmer-panier").click()
    def get_total(self):
        return self.driver.find_element(By.ID, "montant-total").text
    def get_net(self):
        return self.driver.find_element(By.ID, "montant-net").text
    def is_payment_enabled(self):
        btn = self.driver.find_element(By.ID, "realiser-paiement")
        return btn.is_enabled()
    def is_cart_form_present(self):
        return bool(self.driver.find_elements(By.ID, "form-mon-panier"))

