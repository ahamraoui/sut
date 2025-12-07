from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_paiement_cb_valide():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    # Authentification simulée, panier prêt et adresse renseignée
    driver.find_element(By.ID, "cb-numero").send_keys("4111111111111111")
    driver.find_element(By.ID, "cb-expiration").send_keys("12/27")
    driver.find_element(By.ID, "cb-cvc").send_keys("123")
    driver.find_element(By.ID, "confirmer-paiement-cb").click()
    recap = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "recapitulatif-paiement"))
    )
    assert recap.is_displayed()
    driver.quit()

def test_paiement_cb_sans_adresse():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    # Authentification simulée, panier prêt et pas d'adresse
    popup = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "popup-adresse"))
    )
    assert popup.is_displayed()
    lien = driver.find_element(By.ID, "lien-mon-profil")
    assert lien.is_displayed()
    driver.quit()

def test_paiement_cb_refuse():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/paiement")
    # Authentification simulée, panier prêt et adresse renseignée
    driver.find_element(By.ID, "cb-numero").send_keys("0000000000000000")
    driver.find_element(By.ID, "cb-expiration").send_keys("01/20")
    driver.find_element(By.ID, "cb-cvc").send_keys("000")
    driver.find_element(By.ID, "confirmer-paiement-cb").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "cb-erreur"))
    )
    assert error.is_displayed()
    numero = driver.find_element(By.ID, "cb-numero").get_attribute("value")
    assert numero == ""
    driver.quit()

