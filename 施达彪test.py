from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

username='tvh753'
password='a8719941'
chrome_options=webdriver.ChromeOptions()
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
base_url='https://github.com/'
url = base_url+'login'

try:
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.NAME, 'login')))
    time.sleep(1)
    input.send_keys(username)
    time.sleep(1)
    input2 = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    input2.send_keys(password)
    time.sleep(1)
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block')))
    submit.click()
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > img')))
    submit.click()
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')))
    submit.click()
except NoSuchElementException:
    print('Not Found')