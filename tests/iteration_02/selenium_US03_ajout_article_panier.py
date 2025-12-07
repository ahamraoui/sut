from selenium import webdriver
from pages.boutique_page import BoutiquePage

def test_ajout_article_par_code():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/boutique")
    page = BoutiquePage(driver)
    page.search_article("CODE123")
    articles = page.get_articles()
    assert len(articles) > 0
    page.add_article_to_cart()
    assert page.get_cart_count() >= 1
    driver.quit()

def test_ajout_article_par_mot_cle():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/boutique")
    page = BoutiquePage(driver)
    page.search_article("chaussure")
    articles = page.get_articles()
    assert len(articles) > 0
    page.add_article_to_cart()
    assert page.get_cart_count() >= 1
    driver.quit()

def test_ajout_article_indisponible():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/boutique")
    page = BoutiquePage(driver)
    page.search_article("ARTICLE_INDISPONIBLE")
    color = page.get_unavailable_btn_color()
    assert color == "rgb(255, 0, 0)"  # rouge
    page.add_unavailable_article()
    assert page.get_cart_count() == 0
    driver.quit()
