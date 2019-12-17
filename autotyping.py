from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pyautogui
import time
from timeit import default_timer as timer
import random

print('What length of test would you like? Please enter 1, 3, or 5.')
length = input()

print('Would you like Random Text, Sentences, or Words?')
test = input()
if test == 'Random Text':
    test = '#text5'
elif test == 'Sentences':
    test = '#text3'
elif test == 'Words':
    test = '#text1'
else:
    print('Defaulting to Random Text')
    test = '#text5'

print('Starting test...')
with webdriver.Firefox(executable_path=r'C:\PythonLearning\geckodriver.exe') as driver:

    wait = WebDriverWait(driver, 10)
    PAGE = "https://typingtest.com"
    driver.get(PAGE)

    driver.find_element_by_css_selector(f'#time{length}').click()

    driver.find_element_by_css_selector('.start-btn').click()
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    wordList = soup.find_all('span')

    char = []
    for word in range(10, len(wordList)-11):
        try:
            char.append(wordList[word].text)
        except:
            break

    print(len(char))
    print(len(wordList))
    start = timer()
    for appendedWord in range(len(char)):
        pyautogui.typewrite(str(char[appendedWord]))
        pyautogui.press('space')
        end = timer()
        print(end)
        if (end-start) > 60:
            break

    time.sleep(10)
    typingSpeed = driver.find_element_by_css_selector('.speed > span:nth-child(2)').text
    print(f'You typed at {typingSpeed} wpm.')
