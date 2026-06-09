import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def try_xp(driver, xpath, wait=0):
    """Tries to find an element by XPath, optionally waiting for it."""
    try:
        if wait > 0:
            return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
        else:
            return driver.find_element(By.XPATH, xpath)
    except (NoSuchElementException, TimeoutException):
        return None

def scroll_to_view(driver, element, align_top=True):
    """Scrolls an element into view using JS."""
    try:
        driver.execute_script("arguments[0].scrollIntoView(arguments[1]);", element, align_top)
        time.sleep(0.5)
    except Exception:
        pass

def wait_and_click(driver, by, identifier, timeout=10):
    """Waits for an element to be clickable and clicks it."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, identifier))
        )
        element.click()
        return True
    except Exception as e:
        print(f"Failed to wait and click {identifier}: {e}")
        return False
