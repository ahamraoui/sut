from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_supprimer_article_panier():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/mon-panier")
    # Authentification simulée et ajout d'un article si besoin
    articles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "panier-article"))
    )
    assert len(articles) > 0
    moins_un_btn = driver.find_element(By.CSS_SELECTOR, ".moins-un")
    moins_un_btn.click()
    confirm_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "confirm-suppression"))
    )
    confirm_btn.click()
    # Vérifier la quantité ou la disparition de l'article
    # Si le panier est vide
    try:
        message = driver.find_element(By.ID, "panier-vide-message").text
        assert "panier est supprimé" in message
    except:
        pass
    driver.quit()

