import datetime

import action as action
from selenium import webdriver
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/wait1.html"

import math



try:
    browser = webdriver.Chrome()
    browser.maximize_window()  # окно на весь экран
    browser.get(link)
    verifybutton = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify')))
    verifybutton.click() #Ожидание кликабельности элемента
    message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "verify_message")))
    assert "successful" in message.text #Смотрим частичное совпаданиe сообщения с текстом







finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    browser.quit()
