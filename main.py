
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Путь к драйверу браузера
DRIVER_PATH = 'D:\chromedriver.exe'

# Инициализация сервиса
service = Service(DRIVER_PATH)
service.start()
print("Работа начата!")

# Инициализация драйвера браузера
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# URL страницы
url = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=USD_RUB'

# Загрузка страницы
driver.get(url)

# Выполнение JavaScript кода (если необходимо)
# driver.execute_script("ваш_код_JavaScript")
#
# # Получение содержимого таблицы
table = driver.find_element_by_xpath('//table')
# rows = table.find_elements_by_xpath('.//tr')
#
# # Обработка данных таблицы
# data = []
# for row in rows:
#     cols = row.find_elements_by_xpath('.//td')
#     cols = [col.text.strip() for col in cols]
#     data.append(cols)
#
# # Закрытие браузера


# Далее обработка данных и сохранение их в файл Excel, как было показано ранее


input("Нажмите Enter для завершения работы и закрытия браузера")

driver.quit()
print("Работа окончена!")
