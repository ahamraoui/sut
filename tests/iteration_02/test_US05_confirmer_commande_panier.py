from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est authentifié et a au moins un article dans son panier")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et ajout d'un article si besoin

@given("l'internaute est authentifié et son panier est vide")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et vider le panier si besoin

@when('il accède à la page "Mon panier"')
def step_impl(context):
    context.driver.get("https://votre-plateforme/mon-panier")

@when('il clique sur le bouton "Confirmer le panier"')
def step_impl(context):
    context.driver.find_element(By.ID, "confirmer-panier").click()

@then('le montant total, les remises éventuelles et le montant net à payer s\'affichent')
def step_impl(context):
    total = context.driver.find_element(By.ID, "montant-total").text
    net = context.driver.find_element(By.ID, "montant-net").text
    assert total and net

@then('le bouton "Réaliser mon paiement" est actif')
def step_impl(context):
    btn = context.driver.find_element(By.ID, "realiser-paiement")
    assert btn.is_enabled()

@then('le formulaire "Mon panier" ne s\'affiche pas')
def step_impl(context):
    assert not context.driver.find_elements(By.ID, "form-mon-panier")

