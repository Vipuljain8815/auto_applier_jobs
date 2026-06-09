

###################################################### APPLICATION INPUTS ######################################################

## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

import os
from config.env_loader import load_env
load_env()

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = int(os.getenv("EXPECTED_SALARY"))          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = int(os.getenv("CURRENT_SALARY"))            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = int(os.getenv("NOTICE_PERIOD"))                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = os.getenv("LINKEDIN_HEADLINE")

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = os.getenv("LINKEDIN_SUMMARY")

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = os.getenv("COVER_LETTER")
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all = (
    f"Total Experience: {os.getenv('TOTAL_EXPERIENCE')} years\n"
    f"Current Salary: {os.getenv('CURRENT_SALARY')}\n"
    f"Expected Salary: {os.getenv('EXPECTED_SALARY')}\n"
    "Technologies: \n"
    f"- {os.getenv('SEARCH_LANGUAGES')}: {os.getenv('TOTAL_EXPERIENCE')} years\n"
    "- No experience in other programming languages (0 years).\n"
    f"Location: {os.getenv('SEARCH_LOCATION')}\n"
    f"Immediate Joiner: {'Yes' if str(os.getenv('IS_IMMEDIATE')).lower() == 'yes' else 'No'}\n"
    f"Notice Period: {os.getenv('NOTICE_PERIOD')} days\n"
)
##<

# Name of your most recent employer
recent_employer = os.getenv("RECENT_EMPLOYER")

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = os.getenv("CONFIDENCE_LEVEL")
##



# >>>>>>>>>>> NAUKRI SPECIFIC SETTINGS <<<<<<<<<<<
# If a question contains these keys, answer with the given value
questions_mapping = {
    "flutter": os.getenv("TOTAL_EXPERIENCE"),
    "dart": os.getenv("TOTAL_EXPERIENCE"),
    "graphql": "5",
    "experience": os.getenv("TOTAL_EXPERIENCE"),
    "years": os.getenv("TOTAL_EXPERIENCE"),
    "excepted_salary": os.getenv("EXPECTED_SALARY"),
    "ctc": os.getenv("EXPECTED_SALARY"),
    "current_salary": os.getenv("CURRENT_SALARY"),
    "notice": f"{os.getenv('NOTICE_PERIOD')} days",
    "joiner": "immediate" if str(os.getenv("IS_IMMEDIATE")).lower() == "yes" else "not immediate",
    "current_location": os.getenv("SEARCH_LOCATION"),
    "preferred": os.getenv("SEARCH_LOCATION")
}
# Any other specific language should be 0 because of "no other languages exp"
default_language_exp = "0"

# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = str(os.getenv("PAUSE_BEFORE_SUBMIT")).lower() == "true"

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = str(os.getenv("PAUSE_AT_FAILED_QUESTION")).lower() == "true"
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = str(os.getenv("OVERWRITE_PREVIOUS_ANSWERS")).lower() == "true"

default_resume_path = ""
years_of_experience = str(os.getenv("TOTAL_EXPERIENCE", "0"))

