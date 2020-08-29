from selenium import webdriver
import time
import math

# объявляем драйвер
browser = webdriver.Chrome()
# URL страницы теста
link = "http://suninjuly.github.io/math.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
