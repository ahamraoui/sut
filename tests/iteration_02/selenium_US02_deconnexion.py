from selenium import webdriver
from pages.login_page import PersonalSpacePage

def test_deconnexion_reussie():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/espace-personnel")
    page = PersonalSpacePage(driver)
    page.logout()
    assert page.is_redirected_to_login()
    assert "déconnexion" in page.get_logout_message()
    driver.quit()
