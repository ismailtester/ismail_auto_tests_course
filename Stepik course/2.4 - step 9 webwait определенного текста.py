import datetime

import action as action
import pyperclip as pyperclip
from selenium import webdriver
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.maximize_window()  # окно на весь экран
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print("Элемент найден")
    book = browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    #Копирование кода в буфер обмена
    alert = browser.switch_to.alert.text
    addToClipBoard = alert.split(': ')[-1]
    pyperclip.copy(addToClipBoard)







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    browser.quit()
