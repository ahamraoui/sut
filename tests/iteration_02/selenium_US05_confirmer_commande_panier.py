from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_confirmer_panier_avec_article():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et ajout d'un article si besoin
    driver.find_element(By.ID, "confirmer-panier").click()
    total = driver.find_element(By.ID, "montant-total").text
    net = driver.find_element(By.ID, "montant-net").text
    assert total and net
    btn = driver.find_element(By.ID, "realiser-paiement")
    assert btn.is_enabled()
    driver.quit()

def test_confirmer_panier_vide():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et vider le panier si besoin
    assert not driver.find_elements(By.ID, "form-mon-panier")
    driver.quit()

