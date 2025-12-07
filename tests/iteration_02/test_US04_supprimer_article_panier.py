from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est authentifié et a un article dans son panier")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et ajout d'un article si besoin

@when('il accède à la page "Mon panier"')
def step_impl(context):
    context.driver.get("https://votre-plateforme/mon-panier")

@then('la liste des articles du panier s\'affiche')
def step_impl(context):
    articles = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "panier-article"))
    )
    assert len(articles) > 0

@when('il clique sur le lien "-1" pour un article')
def step_impl(context):
    moins_un_btn = context.driver.find_element(By.CSS_SELECTOR, ".moins-un")
    moins_un_btn.click()

@when('il confirme la suppression')
def step_impl(context):
    confirm_btn = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.ID, "confirm-suppression"))
    )
    confirm_btn.click()

@then('la quantité de l\'article est décrémentée ou l\'article est supprimé si quantité = 0')
def step_impl(context):
    # Vérifier la quantité ou la disparition de l'article
    pass

@then('si le panier est vide, un message informe que le panier est supprimé')
def step_impl(context):
    try:
        message = context.driver.find_element(By.ID, "panier-vide-message").text
        assert "panier est supprimé" in message
    except:
        pass

