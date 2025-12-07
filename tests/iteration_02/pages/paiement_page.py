from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaiementPage:
    def __init__(self, driver):
        self.driver = driver
    def enter_cb_info(self, numero, expiration, cvc):
        self.driver.find_element(By.ID, "cb-numero").send_keys(numero)
        self.driver.find_element(By.ID, "cb-expiration").send_keys(expiration)
        self.driver.find_element(By.ID, "cb-cvc").send_keys(cvc)
    def confirm_payment(self):
        self.driver.find_element(By.ID, "confirmer-paiement-cb").click()
    def get_recap(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "recapitulatif-paiement"))
        )
    def get_popup_adresse(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "popup-adresse")))
    def get_lien_profil(self):
        return self.driver.find_element(By.ID, "lien-mon-profil")
    def get_error(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "cb-erreur"))
        )
    def get_cb_numero_value(self):
        return self.driver.find_element(By.ID, "cb-numero").get_attribute("value")

