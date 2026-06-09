import sys
import os

# Import necessary config and helpers
from config.secrets import gmail_username, gmail_app_password
from modules.linkedin_feed import check_feed_and_apply

def main():
    print("--- Starting LinkedIn Feed Applier ---")
    
    resume_path = os.path.expanduser("~/Downloads/Vipul_Jain_Resume.pdf")
    if not os.path.exists(resume_path):
        print(f"Error: Resume not found at {resume_path}")
        print("Please ensure the file is there or update the path.")
        sys.exit(1)
        
    if gmail_app_password == "your_gmail_app_password_here":
        print("Error: You have not configured your Gmail App Password in config/secrets.py.")
        print("Please update GMAIL_APP_PASSWORD and try again.")
        sys.exit(1)

    # Initialize driver (imports open_chrome which initializes driver on import)
    try:
        from modules.open_chrome import driver
        from modules.linkedin_main import is_logged_in_LN, login_LN
        
        # Set page load timeout to prevent hanging indefinitely
        driver.set_page_load_timeout(30)
        
        try:
            # Navigate to the home page so we can accurately check if we are logged in
            driver.get("https://www.linkedin.com/")
        except Exception as e:
            print(f"Page load timeout or error (ignoring): {e}")

        # Check login
        if not is_logged_in_LN():
            login_LN()
            
        # Run feed checker
        check_feed_and_apply(driver, gmail_username, gmail_app_password, resume_path, max_scrolls=None)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    main()
