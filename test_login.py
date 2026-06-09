import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
time.sleep(5)
with open("fresh_login.html", "w") as f:
    f.write(driver.page_source)
driver.quit()
