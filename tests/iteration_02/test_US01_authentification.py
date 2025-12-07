from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est sur la page de connexion")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/login")

@when("il saisit un identifiant et un mot de passe valides")
def step_impl(context):
    context.driver.find_element(By.ID, "login").send_keys("user")
    context.driver.find_element(By.ID, "password").send_keys("pass")

@when("il saisit un identifiant ou un mot de passe invalide")
def step_impl(context):
    context.driver.find_element(By.ID, "login").send_keys("user")
    context.driver.find_element(By.ID, "password").send_keys("wrongpass")

@when("il clique sur le bouton \"Se connecter\"")
def step_impl(context):
    context.driver.find_element(By.ID, "submit").click()

@then("il est redirigé vers son espace personnel")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/espace-personnel")
    )

@then("un message de bienvenue s'affiche")
def step_impl(context):
    message = context.driver.find_element(By.ID, "welcome-message").text
    assert "Bienvenue" in message

@then("un message d'erreur s'affiche")
def step_impl(context):
    error = context.driver.find_element(By.ID, "login-error").text
    assert error != ""

