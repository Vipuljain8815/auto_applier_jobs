


###################################################### CONFIGURE YOUR TOOLS HERE ######################################################


import os
from config.env_loader import load_env
load_env()

# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Your legal name
first_name = os.getenv("FIRST_NAME")                 # Your first name in quotes Eg: "First", "Sai"
middle_name = os.getenv("MIDDLE_NAME")            # Your name in quotes Eg: "Middle", "Vignesh", ""
last_name = os.getenv("LAST_NAME")                # Your last name in quotes Eg: "Last", "Golla"
full_name = f"{first_name} {middle_name} {last_name}".replace("  ", " ").strip()

# Phone number (required), make sure it's valid.
phone_number = os.getenv("PHONE_NUMBER")        # Enter your 10 digit number in quotes Eg: "9876543210"

# What is your current city?
current_city = str(os.getenv("SEARCH_LOCATION")).split(" or ")[0]                  # Los Angeles, San Francisco, etc.

# Address, not so common question but some job applications make it required!
street = os.getenv("STREET")
state = os.getenv("STATE")
zipcode = os.getenv("ZIPCODE")
country = os.getenv("COUNTRY")

## US Equal Opportunity questions
ethnicity = os.getenv("ETHNICITY")              # "Decline", "Hispanic/Latino", "American Indian or Alaska Native", "Asian", "Black or African American", "Native Hawaiian or Other Pacific Islander", "White", "Other"
gender = os.getenv("GENDER")                 # "Male", "Female", "Other", "Decline" or ""
disability_status = os.getenv("DISABILITY_STATUS")      # "Yes", "No", "Decline"
veteran_status = os.getenv("VETERAN_STATUS")         # "Yes", "No", "Decline"
##

require_visa = os.getenv("REQUIRE_VISA")
us_citizenship = os.getenv("US_CITIZENSHIP")
linkedIn = os.getenv("LINKEDIN_URL")
website = os.getenv("WEBSITE_URL")
