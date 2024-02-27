from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Путь к драйверу браузера
DRIVER_PATH = 'D:\chromedriver.exe'

# URL страницы
url = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=USD_RUB'

# Инициализация драйвера браузера
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Загрузка страницы
driver.get(url)

try:
    # Ждем появления кнопки "Согласен" в течение 10 секунд
    accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn2 btn2-primary' and contains(text(), 'Согласен')]")))
    # Если кнопка найдена, нажимаем на неё
    accept_button.click()
    print("Кнопка 'Согласен' найдена и нажата.")
except TimeoutException:
    # Если кнопка не найдена в течение 10 секунд, выводим сообщение и продолжаем выполнение без нажатия
    print("Кнопка 'Согласен' не найдена.")
    pass









# Ждем загрузки динамической таблицы
dynamic_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

# Получаем строки таблицы
table_rows = dynamic_table.find_elements(By.CSS_SELECTOR, "tr")

# Проходимся по каждой строке и выводим текст ячеек
for row in table_rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    print(row_data)


input("Нажмите Enter для завершения работы и закрытия браузера")

driver.quit()
print("Работа окончена!")