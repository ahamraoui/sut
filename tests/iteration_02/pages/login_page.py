from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def login(self, username, password):
        self.driver.find_element(By.ID, "login").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()
    def get_welcome_message(self):
        return self.driver.find_element(By.ID, "welcome-message").text
    def get_error_message(self):
        return self.driver.find_element(By.ID, "login-error").text
    def is_redirected_to_personal_space(self):
        return "/espace-personnel" in self.driver.current_url

class PersonalSpacePage:
    def __init__(self, driver):
        self.driver = driver
    def logout(self):
        self.driver.find_element(By.ID, "logout").click()
    def get_logout_message(self):
        return self.driver.find_element(By.ID, "logout-message").text
    def is_redirected_to_login(self):
        return "/login" in self.driver.current_url

