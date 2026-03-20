from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

def test_search_invalid_film():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()

    invalid_film = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(invalid_film)

    driver.find_element(By.CSS_SELECTOR,
                      'svg[class="styles_icon__a6f9D search-form-submit-button__icon"]').click()
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="search_results_top"]')))
    film = driver.find_element(By.CSS_SELECTOR, 'h2[style="font:100 18px"]').text

    assert film == "К сожалению, по вашему запросу ничего не найдено..."
    driver.quit()
