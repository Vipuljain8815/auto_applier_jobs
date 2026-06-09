import time
import urllib.parse
from selenium.webdriver.common.by import By

def search_jobs(driver, keywords, location, experience_years):
    print(f"Searching for jobs with location: {location} and experience: {experience_years} years.")
    
    for keyword in keywords:
        print(f"Searching for keyword: {keyword}")
        
        encoded_keyword = urllib.parse.quote(keyword)
        encoded_location = urllib.parse.quote(location)
        
        path_keyword = keyword.replace(' ', '-').lower()
        path_location = location.lower()
        
        url = f"https://www.naukri.com/{path_keyword}-jobs-in-{path_location}?k={encoded_keyword}&l={encoded_location}&experience={experience_years}"
        driver.get(url)
        
        # Allow time for the page and job cards to load
        time.sleep(5)
        
        yield keyword
