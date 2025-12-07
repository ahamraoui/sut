from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ajout_article_par_code():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/boutique")
    # Authentification simulée
    # driver.find_element(By.ID, "login").send_keys("user")
    # driver.find_element(By.ID, "password").send_keys("pass")
    # driver.find_element(By.ID, "submit").click()
    search_box = driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("CODE123")
    driver.find_element(By.ID, "search-btn").click()
    articles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "article-item"))
    )
    assert len(articles) > 0
    plus_one_btn = driver.find_element(By.CSS_SELECTOR, ".plus-one.active")
    plus_one_btn.click()
    panier_count = driver.find_element(By.ID, "panier-count").text
    assert int(panier_count) >= 1
    driver.quit()

def test_ajout_article_par_mot_cle():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/boutique")
    search_box = driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("chaussure")
    driver.find_element(By.ID, "search-btn").click()
    articles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "article-item"))
    )
    assert len(articles) > 0
    plus_one_btn = driver.find_element(By.CSS_SELECTOR, ".plus-one.active")
    plus_one_btn.click()
    panier_count = driver.find_element(By.ID, "panier-count").text
    assert int(panier_count) >= 1
    driver.quit()

def test_ajout_article_indisponible():
    driver = webdriver.Chrome()
    driver.get("https://votre-plateforme/boutique")
    search_box = driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys("ARTICLE_INDISPONIBLE")
    driver.find_element(By.ID, "search-btn").click()
    plus_one_btn = driver.find_element(By.CSS_SELECTOR, ".plus-one.inactive")
    color = plus_one_btn.value_of_css_property("color")
    assert color == "rgb(255, 0, 0)"  # rouge
    plus_one_btn.click()
    panier_count = driver.find_element(By.ID, "panier-count").text
    assert int(panier_count) == 0
    driver.quit()

