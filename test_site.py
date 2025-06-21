from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    driver.quit()

def test_open_s6(browser):
    browser.get("https://demoblaze.com/index.html")
    wait = WebDriverWait(browser, 10)

    galaxy_s6 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Samsung galaxy s6')]")))
    galaxy_s6.click()

    title_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[@class='name'][contains(., 'Samsung')]")))
    assert title_element.text == 'Samsung galaxy s6'