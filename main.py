from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://www.python.org/')

WebDriverWait(driver, 2).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div/section/div[1]/div[2]/p[2]/a'))
)

goToLink1 = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[1]/div[2]/p[2]/a')
goToLink1.click()

WebDriverWait(driver, 2).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.text > table:nth-child(18) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(1) > a:nth-child(1)')
))

goToLink2 = driver.find_element(By.CSS_SELECTOR, '.text > table:nth-child(18) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(1) > a:nth-child(1)')
goToLink2.click()