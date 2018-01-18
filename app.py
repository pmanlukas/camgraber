from selenium import webdriver

import time

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")


driver = webdriver.Chrome(chrome_options=options)

driver.get('https://n57.meraki.com/')

#authenticate 
username = driver.find_element_by_id('email')
password = driver.find_element_by_id('password')

username.send_keys('thanh-son.pham@axians.de')
password.send_keys('abcd1234')

driver.find_element_by_name('commit').click()

driver.find_element_by_xpath('//*[@id="login_form"]/div/ul/li[1]/a').click()



 








driver.quit()