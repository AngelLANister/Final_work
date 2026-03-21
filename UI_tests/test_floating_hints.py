from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_floating_hints():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
         (By.CSS_SELECTOR, '#search')))
    driver.find_element(By.CSS_SELECTOR, '#search').click()
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
         (By.CSS_SELECTOR, 'div[class="filmName"]')))
    film_name = driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    film = film_name.find_element(By.TAG_NAME, 'a').text
    for_hint = film[:2]

    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")

    driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(for_hint)
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]')))
    hint_text = driver.find_element(By.CSS_SELECTOR, 'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]').text

    assert hint_text == "Возможно, вы искали"

    driver.quit()
