from selenium import webdriver
from pages.panier_page import PanierPage

def test_supprimer_article_panier():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/mon-panier")
    page = PanierPage(driver)
    articles = page.get_articles()
    assert len(articles) > 0
    page.remove_article()
    page.confirm_removal()
    message = page.get_empty_message()
    if message:
        assert "panier est supprimé" in message
    driver.quit()
