import time
from modules.open_chrome import driver
from modules.linkedin_main import is_logged_in_LN, login_LN
driver.get("https://www.linkedin.com/feed/")
if not is_logged_in_LN():
    login_LN()
time.sleep(5)
with open("feed.html", "w") as f:
    f.write(driver.page_source)
driver.quit()
