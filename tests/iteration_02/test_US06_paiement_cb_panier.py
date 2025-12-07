from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est authentifié, a un panier prêt à payer et une adresse de livraison renseignée")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/paiement")
    # Authentification simulée, panier prêt et adresse renseignée

@given("l'internaute est authentifié, a un panier prêt à payer et aucune adresse de livraison")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/paiement")
    # Authentification simulée, panier prêt et pas d'adresse

@when('il accède à la page de paiement')
def step_impl(context):
    context.driver.get("https://votre-plateforme/paiement")

@when('il renseigne les informations de carte bancaire valides')
def step_impl(context):
    context.driver.find_element(By.ID, "cb-numero").send_keys("4111111111111111")
    context.driver.find_element(By.ID, "cb-expiration").send_keys("12/27")
    context.driver.find_element(By.ID, "cb-cvc").send_keys("123")

@when('il saisit des informations de carte bancaire invalides')
def step_impl(context):
    context.driver.find_element(By.ID, "cb-numero").send_keys("0000000000000000")
    context.driver.find_element(By.ID, "cb-expiration").send_keys("01/20")
    context.driver.find_element(By.ID, "cb-cvc").send_keys("000")

@when('il clique sur "Confirmer paiement CB"')
def step_impl(context):
    context.driver.find_element(By.ID, "confirmer-paiement-cb").click()

@then('le paiement est enregistré et un récapitulatif s\'affiche')
def step_impl(context):
    recap = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "recapitulatif-paiement"))
    )
    assert recap.is_displayed()

@then('un message popup demande de renseigner l\'adresse de livraison et un lien vers "Mon Profil" est affiché')
def step_impl(context):
    popup = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "popup-adresse"))
    )
    assert popup.is_displayed()
    lien = context.driver.find_element(By.ID, "lien-mon-profil")
    assert lien.is_displayed()

@then('un message d\'erreur s\'affiche et les champs CB sont réinitialisés')
def step_impl(context):
    error = WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.ID, "cb-erreur"))
    )
    assert error.is_displayed()
    numero = context.driver.find_element(By.ID, "cb-numero").get_attribute("value")
    assert numero == ""

