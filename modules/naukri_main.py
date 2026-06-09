import sys
import time
from config.secrets import naukri_username as username, naukri_password as password
from config.search import search_terms as keywords, search_location, current_experience
from config.settings import naukri_max_pages as max_pages, file_name as history_file
from modules.naukri_helpers import print_lg
from modules.naukri_browser import init_browser
from modules.naukri_login import login_to_naukri
from modules.naukri_search import search_jobs
from modules.naukri_apply import apply_to_jobs

def main():
    print_lg("Initializing Naukri Auto Job Applier...")
    
    if not username or not password or username == "your_naukri_email@example.com":
        print_lg("Please update your .env file with your real Naukri credentials before running.")
        sys.exit(1)
    
    # 1. Initialize Browser
    driver = init_browser()
    
    try:
        # 2. Login to Naukri
        print_lg("Attempting to login...")
        login_success = login_to_naukri(driver, username, password)
        if not login_success:
            print_lg("Login failed. Exiting.")
            sys.exit(1)
            
        # 3. Search for jobs and iterate
        search_iterator = search_jobs(driver, keywords, search_location, str(current_experience))
        
        for keyword in search_iterator:
            print_lg(f"Applying to jobs for keyword: {keyword}")
            
            # 4. Apply to the jobs found on the search pages
            apply_to_jobs(driver, max_pages, history_file)
            
            print_lg(f"Finished applications for {keyword}.\n")
            
    except Exception as e:
        print_lg(f"An unexpected error occurred: {e}")
    finally:
        print_lg("Closing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()
        print_lg("Browser closed. Run complete.")

if __name__ == "__main__":
    main()
