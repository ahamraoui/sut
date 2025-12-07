from selenium import webdriver
from pages.paiement_page import PaiementPage

def test_paiement_cb_valide():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    page = PaiementPage(driver)
    page.enter_cb_info("4111111111111111", "12/27", "123")
    page.confirm_payment()
    recap = page.get_recap()
    assert recap.is_displayed()
    driver.quit()

def test_paiement_cb_sans_adresse():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    page = PaiementPage(driver)
    popup = page.get_popup_adresse()
    assert popup.is_displayed()
    lien = page.get_lien_profil()
    assert lien.is_displayed()
    driver.quit()

def test_paiement_cb_refuse():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    page = PaiementPage(driver)
    page.enter_cb_info("0000000000000000", "01/20", "000")
    page.confirm_payment()
    error = page.get_error()
    assert error.is_displayed()
    numero = page.get_cb_numero_value()
    assert numero == ""
    driver.quit()
