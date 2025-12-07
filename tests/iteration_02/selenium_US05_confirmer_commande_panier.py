from selenium import webdriver
from pages.panier_page import PanierPage

def test_confirmer_panier_avec_article():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/mon-panier")
    page = PanierPage(driver)
    page.confirm_cart()
    total = page.get_total()
    net = page.get_net()
    assert total and net
    assert page.is_payment_enabled()
    driver.quit()

def test_confirmer_panier_vide():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/mon-panier")
    page = PanierPage(driver)
    assert not page.is_cart_form_present()
    driver.quit()
