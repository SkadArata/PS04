import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Логирование для диагностики
import logging

logging.basicConfig(level=logging.INFO)

# Инициализация драйвера
browser = webdriver.Chrome()

# Проверка версии Selenium
logging.info(f"Selenium version: {selenium.__version__}")

# Открываем страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем заголовок страницы
assert "Википедия" in browser.title

# Находим окно поиска
search_box = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)

# Вводим текст в строку поиска
search_box.send_keys("Солнечная система")

# Отправляем текст (имитируем нажатие Enter)
search_box.send_keys(Keys.RETURN)

# Ожидаем, пока появится ссылка "Солнечная система" на странице результатов поиска
try:
    a = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Солнечная система"))
    )
    logging.info("Ссылка 'Солнечная система' найдена.")
    # Кликаем по ссылке "Солнечная система"
    a.click()
except selenium.common.exceptions.TimeoutException as e:
    logging.error("Ссылка 'Солнечная система' не найдена.")
    browser.quit()
    raise e

# Ожидаем некоторое время, чтобы увидеть результат (можно заменить на нужные действия)
WebDriverWait(browser, 10).until(
    EC.title_contains("Солнечная система")
)

logging.info("Открыта страница 'Солнечная система'.")

# Закрываем браузер
browser.quit()