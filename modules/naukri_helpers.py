import os
import csv
import time

def print_lg(*args, **kwargs):
    """Simple logging function."""
    print(*args, **kwargs)

def buffer(seconds):
    """Sleep function."""
    time.sleep(seconds)

def get_applied_job_ids(file_name):
    """Reads the applied job IDs from a CSV file."""
    job_ids = set()
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        job_ids.add(row[0])
    except Exception as e:
        print_lg(f"Could not read {file_name}: {e}")
    return job_ids

def get_saved_company_urls(file_name):
    """Reads the saved company URLs from a CSV file to avoid duplicates."""
    urls = set()
    try:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 3 and row[3]:
                        urls.add(row[3])
    except Exception as e:
        print_lg(f"Could not read {file_name}: {e}")
    return urls

def save_applied_job_id(file_name, job_id, job_title, company, job_url=""):
    """Saves a successfully applied job ID to the CSV file."""
    try:
        with open(file_name, 'a', encoding='utf-8', newline='') as file:
            fieldnames = ['Job ID', 'Title', 'Company', 'Job Link', 'External Job link', 'Date Applied']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0: writer.writeheader()
            writer.writerow({'Job ID': job_id, 'Title': job_title, 'Company': company, 'Job Link': job_url, 'External Job link': '', 'Date Applied': time.strftime('%Y-%m-%d %H:%M:%S')})
    except Exception as e:
        print_lg(f"Could not save to {file_name}: {e}")

def save_company_website_job(file_name, job_id, job_title, company, job_url):
    """Saves jobs that require applying on the company website to a separate CSV."""
    try:
        with open(file_name, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([job_id, job_title, company, job_url])
    except Exception as e:
        print_lg(f"Could not save company job to {file_name}: {e}")
