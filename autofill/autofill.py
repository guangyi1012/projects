import time
from datetime import datetime
from selenium import webdriver 

today = datetime.now().strftime("%#m/%d/%Y")

url = "https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAZAALYxrthUNFhTMzJDNTlBME9JNktJS0Y4Q044V1BCNC4u"

x_path_1 = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div/div/input'
x_path_2 = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div/label/input'
x_path_3 = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/div/div/div/input[1]'
x_path_submit = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/button/div'

driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_xpath(x_path_1).send_keys('test')
driver.find_element_by_xpath(x_path_2).click()
driver.find_element_by_xpath(x_path_3).send_keys(today)

driver.find_element_by_xpath(x_path_submit).click()


driver.quit()
