from selenium import webdriver
from pages.remise_page import RemisePage

def test_remise_10_pourcent():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_remise_anciennete()
    remise = page.get_remise_appliquee()
    assert remise == 0.10
    driver.quit()

def test_remise_5_pourcent_premiere_commande():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_remise_premiere_commande()
    remise = page.get_remise_appliquee()
    assert remise == 0.05
    driver.quit()

def test_remise_7_pourcent_vip():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_remise_vip()
    remise = page.get_remise_appliquee()
    assert remise == 0.07
    driver.quit()

def test_remise_5_pourcent_10_commandes():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_remise_10_commandes()
    remise = page.get_remise_appliquee()
    assert remise == 0.05
    driver.quit()

def test_remise_code_promo_prioritaire():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_code_promo()
    remise = page.get_remise_appliquee()
    assert remise == "PROMO"
    driver.quit()

def test_remises_non_cumulables():
    driver = webdriver.Chrome()
    page = RemisePage(driver)
    page.appliquer_remise_prioritaire()
    remise = page.get_remise_appliquee()
    assert remise is not None
    driver.quit()
