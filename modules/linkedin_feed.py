import re
import csv
import time
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from modules.email_sender import send_application_email
from modules.helpers import print_lg
from config.settings import add_comment_to_feed_posts

CSV_FILE = "all excels/all_emails_sent_history.csv"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Author", "Email Found", "Subject Sent", "Comment Added", "Status"])

def log_email_sent(author, email, subject, comment_added, status):
    init_csv()
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), author, email, subject, comment_added, status])

def extract_emails(text):
    # Regex to find email addresses
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def add_comment(driver, post_element, comment_text):
    try:
        # Find the comment button within the post
        comment_btn = post_element.find_element(By.XPATH, './/button[contains(@aria-label, "Comment")]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", comment_btn)
        time.sleep(1)
        comment_btn.click()
        
        time.sleep(2) # wait for the comment box to expand
        
        # Find the editor (LinkedIn uses contenteditable divs for comments)
        editor = post_element.find_element(By.XPATH, './/div[contains(@class, "ql-editor")]')
        editor.click()
        time.sleep(1)
        
        # Type the comment
        editor.send_keys(comment_text)
        time.sleep(1)
        
        # Find the submit button
        submit_btn = post_element.find_element(By.XPATH, './/button[contains(@class, "comments-comment-box__submit-button") or contains(span, "Post")]')
        submit_btn.click()
        time.sleep(2)
        return True
    except Exception as e:
        print_lg(f"Error adding comment: {e}")
        return False

def check_feed_and_apply(driver, gmail_user, gmail_password, resume_path, max_scrolls=None):
    print_lg("Starting LinkedIn feed checker...")
    
    if driver.current_url != "https://www.linkedin.com/feed/":
        try:
            driver.get("https://www.linkedin.com/feed/")
        except Exception:
            pass
        time.sleep(5)
        
    init_csv()
    
    processed_posts = set()
    scrolls = 0
    
    while max_scrolls is None or scrolls < max_scrolls:
        if max_scrolls is None:
            print_lg(f"Scrolling feed... (Scroll {scrolls+1}/∞)")
        else:
            print_lg(f"Scrolling feed... (Scroll {scrolls+1}/{max_scrolls})")
        
        # Find all feed posts currently visible
        # LinkedIn feed posts usually have a class like 'feed-shared-update-v2'
        posts = driver.find_elements(By.XPATH, '//div[contains(@data-urn, "urn:li:activity:")]')
        print_lg(f"Found {len(posts)} posts on this scroll.")
        
        for post in posts:
            try:
                post_urn = post.get_attribute("data-urn")
                if post_urn in processed_posts:
                    continue
                
                processed_posts.add(post_urn)
                
                # Check for "See more" button and click it to get full text
                try:
                    see_more = post.find_element(By.XPATH, './/button[contains(@class, "see-more")]')
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", see_more)
                    time.sleep(1)
                    see_more.click()
                    time.sleep(1)
                except NoSuchElementException:
                    pass
                
                from modules.ocr_extractor import extract_text_from_image
                
                # Extract text from post body
                text_content = ""
                try:
                    text_div = post.find_element(By.XPATH, './/div[contains(@class, "feed-shared-update-v2__description-wrapper")]')
                    text_content = text_div.text
                except NoSuchElementException:
                    pass
                
                # Extract text from images using OCR
                try:
                    images = post.find_elements(By.XPATH, './/img[contains(@class, "ivm-view-attr__img--centered") or contains(@class, "update-components-image__image")]')
                    for img in images:
                        src = img.get_attribute("src")
                        if src and src.startswith("http"):
                            ocr_text = extract_text_from_image(src)
                            if ocr_text:
                                text_content += " " + ocr_text
                except NoSuchElementException:
                    pass
                
                if not text_content.strip():
                    continue
                
                # Extract Author
                author_name = "Unknown"
                try:
                    author_elem = post.find_element(By.XPATH, './/span[contains(@class, "update-components-actor__name") or contains(@class, "feed-shared-actor__name")]/span[1]')
                    author_name = author_elem.text.strip()
                except NoSuchElementException:
                    pass
                
                text_lower = text_content.lower()
                has_flutter = "flutter" in text_lower or "dart" in text_lower

                if has_flutter:
                    emails = extract_emails(text_content)
                    if emails:
                        print_lg(f"Found Flutter-related post by {author_name} with email(s): {emails}")
                        # Remove duplicates
                        emails = list(set(emails))
                        
                        for email in emails:
                            # Send email application
                            subject = f"Application for Flutter role posted by {author_name} on LinkedIn"
                            body = "Hello,\n\nI saw your post on LinkedIn regarding a Flutter opportunity and I am very interested. Please find my resume attached.\n\nBest regards,\nVipul Jain"
                            
                            success = send_application_email(email, subject, body, resume_path, gmail_user, gmail_password)
                            status = "Sent" if success else "Failed"
                            
                            # Add comment if successful and configured
                            comment_added = "No"
                            if success and add_comment_to_feed_posts:
                                comment_text = "Interested! I have sent my resume via email."
                                comment_success = add_comment(driver, post, comment_text)
                                if comment_success:
                                    comment_added = "Yes"
                                    print_lg(f"Successfully added comment to {author_name}'s post.")
                            
                            log_email_sent(author_name, email, subject, comment_added, status)
                    else:
                        print_lg(f"Found Flutter-related post by {author_name} but no email. Adding comment.")
                        if add_comment_to_feed_posts:
                            resume_link = os.getenv("DRIVE_RESUME_LINK", "")
                            
                            if re.search(r'(comment|type|write|drop)\s+.*interested', text_lower) or "#interested" in text_lower:
                                comment_text = "#interested"
                            else:
                                comment_text = "Interested! I am a Flutter developer with 7+ years of experience. Please let me know how to apply."
                            
                            if re.search(r'(share|upload|drop|link|comment|send|attach)\s+.*resume', text_lower) or "resume link" in text_lower:
                                comment_text += f"\nHere is my resume: {resume_link}"

                            comment_success = add_comment(driver, post, comment_text)
                            comment_added = "Yes" if comment_success else "Failed"
                            log_email_sent(author_name, "N/A", "N/A", comment_added, "Comment Only")
            except Exception as e:
                continue
                
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        scrolls += 1
        
    print_lg("Finished checking LinkedIn feed.")
