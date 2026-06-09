import json
import os
import sys

PREFS_FILE = os.path.join(os.path.dirname(__file__), "user_preferences.json")
ENV_FILE = os.path.join(os.path.dirname(__file__), ".env")

from config.env_loader import load_env
load_env(ENV_FILE)

def prompt(message, default=""):
    """Helper to prompt user with a default value."""
    if default:
        res = input(f"{message} [{default}]: ").strip()
        return res if res else default
    else:
        return input(f"{message}: ").strip()

def update_env_file(env_path, updates):
    if not os.path.exists(env_path):
        return
    
    with open(env_path, "r") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        if "=" in line and not line.startswith("#"):
            key = line.split("=")[0].strip()
            if key in updates:
                val = updates[key]
                if '"' in line or "'" in line:
                    lines[i] = f'{key}="{val}"\n'
                else:
                    lines[i] = f'{key}={val}\n'
                del updates[key]
                
    # Add remaining updates
    for key, val in updates.items():
        lines.append(f'{key}="{val}"\n')
        
    with open(env_path, "w") as f:
        f.writelines(lines)

def run_setup():
    print("\n" + "="*50)
    print("Welcome to the Unified Job Applier Setup!")
    print("Please provide your details. We will save this so you won't have to enter it again.")
    print("="*50 + "\n")
    
    prefs = {}
    env_updates = {}
    
    # Platform
    print("Which platform(s) do you want to apply on? (linkedin/naukri/both)")
    prefs['platform'] = prompt("Platform", os.getenv("PLATFORM", "both")).lower()
    if prefs['platform'] not in ['linkedin', 'naukri', 'both']:
        print("Invalid choice, defaulting to 'both'.")
        prefs['platform'] = 'both'
        
    from config import secrets
    
    # Credentials
    if prefs['platform'] in ['linkedin', 'both']:
        print("\n--- LinkedIn Credentials ---")
        prefs['LINKEDIN_EMAIL_OR_PHONE'] = prompt("LinkedIn Email or Phone", secrets.linkedin_email_or_phone)
        prefs['linkedin_password'] = prompt("LinkedIn Password", secrets.linkedin_password)
        
    if prefs['platform'] in ['naukri', 'both']:
        print("\n--- Naukri Credentials ---")
        prefs['naukri_username'] = prompt("Naukri Username / Email", secrets.naukri_username)
        prefs['naukri_password'] = prompt("Naukri Password", secrets.naukri_password)
        
    # Job specifics
    print("\n--- Job Search Preferences ---")
    env_updates['SEARCH_LANGUAGES'] = prompt("Languages/Skills to search (comma-separated, e.g., Flutter, Dart)", os.getenv("SEARCH_LANGUAGES", "Flutter, Dart"))
    env_updates['TOTAL_EXPERIENCE'] = prompt("Total Experience (in years)", os.getenv("TOTAL_EXPERIENCE", "7"))
    env_updates['SEARCH_LOCATION'] = prompt("Location", os.getenv("SEARCH_LOCATION", "Bangalore"))
    env_updates['EXPECTED_SALARY'] = prompt("Expected Salary (e.g., 1800000)", os.getenv("EXPECTED_SALARY", ""))
    env_updates['CURRENT_SALARY'] = prompt("Current Salary (e.g., 1047500)", os.getenv("CURRENT_SALARY", ""))
    
    # Notice Period
    print("\n--- Notice Period ---")
    is_imm = prompt("Are you an immediate joiner? (yes/no)", os.getenv("IS_IMMEDIATE", "yes")).lower()
    if is_imm.startswith('y'):
        env_updates['IS_IMMEDIATE'] = "yes"
        env_updates['NOTICE_PERIOD'] = "0"
    else:
        env_updates['IS_IMMEDIATE'] = "no"
        env_updates['NOTICE_PERIOD'] = prompt("Notice period in days", os.getenv("NOTICE_PERIOD", "15"))

    # Personals Config
    print("\n--- Personals Config ---")
    env_updates['FIRST_NAME'] = prompt("First Name", os.getenv("FIRST_NAME", ""))
    env_updates['MIDDLE_NAME'] = prompt("Middle Name", os.getenv("MIDDLE_NAME", ""))
    env_updates['LAST_NAME'] = prompt("Last Name", os.getenv("LAST_NAME", ""))
    env_updates['PHONE_NUMBER'] = prompt("Phone Number", os.getenv("PHONE_NUMBER", ""))
    env_updates['STREET'] = prompt("Street", os.getenv("STREET", ""))
    env_updates['STATE'] = prompt("State", os.getenv("STATE", ""))
    env_updates['ZIPCODE'] = prompt("Zipcode", os.getenv("ZIPCODE", ""))
    env_updates['COUNTRY'] = prompt("Country", os.getenv("COUNTRY", ""))
    env_updates['LINKEDIN_URL'] = prompt("LinkedIn URL", os.getenv("LINKEDIN_URL", ""))
    env_updates['WEBSITE_URL'] = prompt("Website/Portfolio URL", os.getenv("WEBSITE_URL", ""))
    
    # Save to user_preferences.json
    with open(PREFS_FILE, "w") as f:
        json.dump(prefs, f, indent=4)
        
    # Save to .env
    update_env_file(ENV_FILE, env_updates)
        
    print("\n" + "="*50)
    print("Setup Complete! Your preferences and personal config have been saved.")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_setup()
