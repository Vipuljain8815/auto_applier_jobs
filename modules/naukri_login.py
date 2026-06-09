import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_naukri(driver, username, password):
    driver.get("https://www.naukri.com/nlogin/login")
    
    try:
        print("\nAttempting automatic login with email and password...")
        
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "usernameField"))
        )
        username_field.clear()
        username_field.send_keys(username)
        
        password_field = driver.find_element(By.ID, "passwordField")
        password_field.clear()
        password_field.send_keys(password)
        
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Login')]")
        login_btn.click()
        
        print("Credentials submitted. Waiting for dashboard...")
        WebDriverWait(driver, 180).until(
            lambda driver: "nlogin/login" not in driver.current_url
        )
        print("Successfully logged into Naukri.")
        return True
    except Exception as e:
        print(f"Failed to login or timed out waiting for manual login: {e}")
        try:
            driver.save_screenshot("login_error.png")
        except:
            pass
        return False
