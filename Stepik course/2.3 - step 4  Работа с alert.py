import datetime

import action as action
import pyperclip as pyperclip
from selenium import webdriver
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/alert_accept.html"

import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.maximize_window()  # окно на весь экран
    browser.get(link)
    action = ActionChains(browser)
    joinbutton = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "input_value"))).text
    y = calc(x)  # Нужный расчет
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submitbutton = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    #Копирование кода в буфер обмена
    alert = browser.switch_to.alert.text
    addToClipBoard = alert.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    print("Тест пройден")










finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    browser.quit()
