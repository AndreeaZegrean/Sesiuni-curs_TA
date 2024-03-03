# SELECTORI
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.elefant.ro/new-account?TargetPipeline=ViewProfileSettings-ViewProfile')
driver.maximize_window()
driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
# identificarea unui element si a trimis textul Monica
driver.find_element(By.ID, 'PostCheckoutRegisterForm_FirstName').send_keys('Monica')
driver.find_element(By.CLASS_NAME, 'form-control').send_keys('Razvan')
driver.find_element(By.NAME, 'PostCheckoutRegisterForm_LastName').send_keys('Zegrean')

#driver.find_element(By.LINK_TEXT, 'Conectare').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Conectare').click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'Cone').click()
# adoarme testul automat pt cat timp setam noi
time.sleep(5)

lista = driver.find_elements(By.CLASS_NAME, 'form-control')
assert len(lista) == 4

