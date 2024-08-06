from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def start_browser():
    # Инициализация драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def search_wikipedia(driver, query):
    driver.get("https://ru.wikipedia.org")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Ожидание загрузки страницы


def read_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, p in enumerate(paragraphs):
        print(f"\nПараграф {i + 1}:\n{p.text}\n")
        next_action = input("Введите 'n' для следующего параграфа, 'm' для меню: ").strip().lower()
        if next_action == 'm':
            break


def list_internal_links(driver):
    links = driver.find_elements(By.XPATH, "//a[@href and not(contains(@href, ':'))]")
    internal_links = {i: link for i, link in enumerate(links) if
                      link.get_attribute('href').startswith('https://ru.wikipedia.org/wiki/')}

    for index, link in internal_links.items():
        print(f"{index}: {link.text}")

    return internal_links


def main():
    driver = start_browser()
    try:
        query = input("Введите запрос для поиска в Википедии: ")
        search_wikipedia(driver, query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Ваш выбор: ").strip()
            if choice == '1':
                read_paragraphs(driver)
            elif choice == '2':
                internal_links = list_internal_links(driver)
                link_choice = int(input("Введите номер ссылки для перехода: ").strip())
                if link_choice in internal_links:
                    internal_links[link_choice].click()
                    time.sleep(3)  # Ожидание загрузки страницы
            elif choice == '3':
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
