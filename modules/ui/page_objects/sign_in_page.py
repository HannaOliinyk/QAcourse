from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'
    
    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
    

class NovaPost(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(NovaPost.URL)

    def try_search_invoice(self, invoice_number):
        invoice_input = self.driver.find_element(By.ID, "cargo_number")
        invoice_input.send_keys(invoice_number)
        btn_elem = self.driver.find_element(By.NAME, "")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title