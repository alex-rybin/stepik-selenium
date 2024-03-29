# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element_by_id('book').click()
    y = calc(int(driver.find_element_by_id('input_value').text))
    driver.find_element_by_id('answer').send_keys(str(y))
    driver.find_element_by_id('solve').click()
    sleep(30)
finally:
    driver.quit()
