import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get("https://github.com/login")
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("a2320@formatmail.com")
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong password")
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()
    assert driver.title == "Sign in to GitHub · GitHub"
    driver.close()

@pytest.mark.ui
def test_check_incorrect_parcel_of_nova_poshta():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get("https://novaposhta.ua/")
    invoice_number = driver.find_element(By.ID, "cargo_number")
    invoice_number.send_keys("45600000034189")
    btn_elem = driver.find_element(By.NAME, "")
    btn_elem.click()
    assert driver.title == "Трекінг посилки | Nova Global"
    driver.close()