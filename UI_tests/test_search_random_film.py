from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_random_film():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    waiter1 = WebDriverWait(driver, 40)
    waiter1.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    waiter2 = WebDriverWait(driver, 40)
    waiter2.until(EC.visibility_of_element_located(
         (By.CSS_SELECTOR, '#search')))
    driver.find_element(By.CSS_SELECTOR, '#search').click()
    waiter3 = WebDriverWait(driver, 40)
    waiter3.until(EC.visibility_of_element_located(
         (By.CSS_SELECTOR, 'div[class="filmName"]')))
    film_name = driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    rnd_film = film_name.find_element(By.TAG_NAME, 'a').text

    driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")

    driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(rnd_film)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    name = driver.find_element(By.CSS_SELECTOR, 'div[class="element most_wanted"]')
    info = name.find_element(By.CSS_SELECTOR, 'div[class="info"]')
    film = info.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text

    assert film == rnd_film

    driver.quit()
