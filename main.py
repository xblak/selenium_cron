from telnetlib import EC

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = os.environ['url']
username = os.environ['username']
password = os.environ['password']

print('hi'+username+', Health Check!')
driver = webdriver.Chrome()
driver.get("https://myclu.callutheran.edu/health-check/?_=1")
assert "Cal Lutheran Login" in driver.title
print('logging in')
loginID = driver.find_element_by_id("frmLogin_UserName")
loginID.send_keys(username)
loginPswd = driver.find_element_by_id("frmLogin_Password")
loginPswd.send_keys(password)
loginBtn = driver.find_element_by_id("btnLogin")
loginBtn.click()
element = WebDriverWait(driver, 10).until(EC.title_is("Daily Health Check"))
print('filling the form')
driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[3]/div[2]/fieldset/div[2]/div[1]/button').click()
# yes
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[1]/div[2]/div[1]/button'))).click()
# no
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[2]/div[2]/div[2]/button'))).click()
# no
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[3]/div[2]/div[2]/button'))).click()
# confirm both
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'//*[@id="confirm_mask"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'//*[@id="confirm"]'))).click()

# put in first and last name
firstname = driver.find_element_by_xpath(r'/html/body/div/div[2]/div[3]/div[5]/div[2]/div[3]/div[1]/label').text
lastname = driver.find_element_by_xpath(r'/html/body/div/div[2]/div[3]/div[5]/div[2]/div[3]/div[2]/label').text
fnIn = driver.find_element_by_id("signature_first_name")
fnIn.send_keys(firstname)
lnIn = driver.find_element_by_id("signature_last_name")
lnIn.send_keys(lastname)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, r'/html/body/div/div[2]/div[3]/div[7]/button'))).click()
print('done')

driver.close()

# def waitForElement(self, XPATH)
#     return
