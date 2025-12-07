from bhave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("l'internaute est authentifié et sur la page \"Boutique\"")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://votre-plateforme/boutique")
    # Authentification simulée (à adapter selon l'application)
    # context.driver.find_element(By.ID, "login").send_keys("user")
    # context.driver.find_element(By.ID, "password").send_keys("pass")
    # context.driver.find_element(By.ID, "submit").click()

@when('il saisit un code article valide dans la barre de recherche')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("CODE123")

@when('il saisit un mot clé dans la barre de recherche')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("chaussure")

@when('il clique sur le bouton "Rechercher"')
def step_impl(context):
    context.driver.find_element(By.ID, "search-btn").click()

@then('la liste des articles correspondants s\'affiche')
def step_impl(context):
    articles = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "article-item"))
    )
    assert len(articles) > 0

@when('il clique sur le lien vert "+1" pour un article disponible')
def step_impl(context):
    plus_one_btn = context.driver.find_element(By.CSS_SELECTOR, ".plus-one.active")
    plus_one_btn.click()

@then('l\'article est ajouté au panier et le nombre d\'articles du panier est incrémenté de 1')
def step_impl(context):
    panier_count = context.driver.find_element(By.ID, "panier-count").text
    assert int(panier_count) >= 1

@when('il recherche un article indisponible')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("ARTICLE_INDISPONIBLE")
    context.driver.find_element(By.ID, "search-btn").click()

@then('le lien "+1" est inactif et de couleur rouge')
def step_impl(context):
    plus_one_btn = context.driver.find_element(By.CSS_SELECTOR, ".plus-one.inactive")
    color = plus_one_btn.value_of_css_property("color")
    assert color == "rgb(255, 0, 0)"  # rouge

@when('il tente de cliquer sur le lien rouge "+1"')
def step_impl(context):
    plus_one_btn = context.driver.find_element(By.CSS_SELECTOR, ".plus-one.inactive")
    plus_one_btn.click()

@then('l\'article n\'est pas ajouté au panier')
def step_impl(context):
    panier_count = context.driver.find_element(By.ID, "panier-count").text
    assert int(panier_count) == 0

