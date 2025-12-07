from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est authentifié et sur son espace personnel")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/espace-personnel")
    # Authentification simulée

@when("il clique sur le bouton \"Déconnexion\"")
def step_impl(context):
    context.driver.find_element(By.ID, "logout").click()

@then("il est redirigé vers la page de connexion")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/login")
    )

@then("un message de confirmation de déconnexion s'affiche")
def step_impl(context):
    message = context.driver.find_element(By.ID, "logout-message").text
    assert "déconnexion" in message

