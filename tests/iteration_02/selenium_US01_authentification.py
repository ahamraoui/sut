from selenium import webdriver
from pages.login_page import LoginPage

def test_authentification_reussie():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")
    page = LoginPage(driver)
    page.login("root", "1234")
    assert page.is_redirected_to_personal_space()
    assert "Bienvenue" in page.get_welcome_message()
    driver.quit()

def test_authentification_echouee():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/accounts/login")
    page = LoginPage(driver)
    page.login("user", "wrongpass")
    assert page.get_error_message() != ""
    driver.quit()
