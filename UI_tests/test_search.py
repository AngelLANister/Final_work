from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#js-button")))
    driver.find_element(By.CSS_SELECTOR, "#js-button").click()
    waiter1 = WebDriverWait(driver, 40)
    waiter1.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()

    driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys("Холоп")

    driver.find_element(By.CSS_SELECTOR,
                      'svg[class="styles_icon__a6f9D search-form-submit-button__icon"]').click()

    name = driver.find_element(By.CSS_SELECTOR, 'div[class="element most_wanted"]')
    info = name.find_element(By.CSS_SELECTOR, 'div[class="info"]')
    a = info.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text

    assert a == "Холоп"

    driver.quit()
