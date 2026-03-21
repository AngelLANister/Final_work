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
    link_film = driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    link_film.find_element(By.CSS_SELECTOR, 'a[href]').click()
    waiter = WebDriverWait(driver, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]')))
    driver.find_element(By.CSS_SELECTOR, 'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]').click()
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')))
    info = driver.find_element(By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')
    film = info.find_element(By.CSS_SELECTOR, 'a[data-tid="kp-ui.section-title.more-link"]').text

    assert film == "Рецензии зрителей"

    driver.quit()
