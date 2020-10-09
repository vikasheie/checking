from Screenshot import Screenshot_Clipping
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



driver=webdriver.Chrome("E:\\chromedriver\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
url = "https://www.google.com"
driver.get(url)
sleep(10)
driver.quit()
print("Success")