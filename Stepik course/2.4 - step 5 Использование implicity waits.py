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
    browser.implicitly_wait(5) #ВКЛЮЧАЕТСЯ ОЖИДАНИЕ ПОСЛЕ КАЖДОГО ДЕЙСТВИЯ
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text






finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    browser.quit()
