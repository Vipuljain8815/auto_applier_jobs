import os
from config.env_loader import load_env
load_env()

# These Sentences are Searched in LinkedIn
# Enter your search terms inside '[ ]' with quotes ' "searching title" ' for each search followed by comma ', ' Eg: ["Software Engineer", "Software Developer", "Selenium Developer"]
search_terms = [lang.strip() for lang in str(os.getenv("SEARCH_LANGUAGES")).split(',')]

# Search location, this will be filled in "City, state, or zip code" search box. If left empty as "", tool will not fill it.
search_location = os.getenv("SEARCH_LOCATION")               # Some valid examples: "", "United States", "India", "Chicago, Illinois, United States", "90001, Los Angeles, California, United States", "Bengaluru, Karnataka, India", etc.

# After how many number of applications in current search should the bot switch to next search? 
switch_number = int(os.getenv("SWITCH_NUMBER"))                 # Only numbers greater than 0... Don't put in quotes

# Do you want to randomize the search order for search_terms?
randomize_search_order = str(os.getenv("RANDOMIZE_SEARCH_ORDER")).lower() == "true"     # True of False, Note: True or False are case-sensitive


# >>>>>>>>>>> Job Search Filters <<<<<<<<<<<

sort_by = os.getenv("SORT_BY")                       # "Most recent", "Most relevant" or ("" to not select) 
date_posted = os.getenv("DATE_POSTED")         # "Any time", "Past month", "Past week", "Past 24 hours" or ("" to not select)
salary = os.getenv("SALARY")                        # "$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+"

easy_apply_only = str(os.getenv("EASY_APPLY_ONLY")).lower() == "true"             # True or False, Note: True or False are case-sensitive

experience_level = str(os.getenv("EXPERIENCE_LEVEL")).split(",") if os.getenv("EXPERIENCE_LEVEL") else []              # (multiple select) "Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"
job_type = str(os.getenv("JOB_TYPE")).split(",") if os.getenv("JOB_TYPE") else []                      # (multiple select) "Full-time", "Part-time", "Contract", "Temporary", "Volunteer", "Internship", "Other"
is_remote = str(os.getenv("REMOTE", "False")).lower() == "true"
on_site = []
if is_remote:
    on_site.append("Remote")
    if search_location.strip():
        on_site.append("On-site")

companies = []                     # (dynamic multiple select) make sure the name you type in list exactly matches with the company name you're looking for, including capitals. 
                                   # Eg: "7-eleven", "Google","X, the moonshot factory","YouTube","CapitalG","Adometry (acquired by Google)","Meta","Apple","Byte Dance","Netflix", "Snowflake","Mineral.ai","Microsoft","JP Morgan","Barclays","Visa","American Express", "Snap Inc", "JPMorgan Chase & Co.", "Tata Consultancy Services", "Recruiting from Scratch", "Epic", and so on...
location = []                      # (dynamic multiple select)
industry = []                      # (dynamic multiple select)
job_function = []                  # (dynamic multiple select)
job_titles = []                    # (dynamic multiple select)
benefits = []                      # (dynamic multiple select)
commitments = []                   # (dynamic multiple select)

under_10_applicants = str(os.getenv("UNDER_10_APPLICANTS")).lower() == "true"        # True or False, Note: True or False are case-sensitive
in_your_network = str(os.getenv("IN_YOUR_NETWORK")).lower() == "true"            # True or False, Note: True or False are case-sensitive
fair_chance_employer = str(os.getenv("FAIR_CHANCE_EMPLOYER")).lower() == "true"       # True or False, Note: True or False are case-sensitive


## >>>>>>>>>>> RELATED SETTING <<<<<<<<<<<

# Pause after applying filters to let you modify the search results and filters?
pause_after_filters = str(os.getenv("PAUSE_AFTER_FILTERS")).lower() == "true"         # True or False, Note: True or False are case-sensitive

##




## >>>>>>>>>>> SKIP IRRELEVANT JOBS <<<<<<<<<<<
 
# Avoid applying to these companies, and companies with these bad words in their 'About Company' section...
about_company_bad_words = str(os.getenv("ABOUT_COMPANY_BAD_WORDS")).split(",") if os.getenv("ABOUT_COMPANY_BAD_WORDS") else []       # (dynamic multiple search) or leave empty as []. Ex: ["Staffing", "Recruiting", "Name of Company you don't want to apply to"]

# Skip checking for `about_company_bad_words` for these companies if they have these good words in their 'About Company' section... [Exceptions, For example, I want to apply to "Robert Half" although it's a staffing company]
about_company_good_words = str(os.getenv("ABOUT_COMPANY_GOOD_WORDS")).split(",") if os.getenv("ABOUT_COMPANY_GOOD_WORDS") else []      # (dynamic multiple search) or leave empty as []. Ex: ["Robert Half", "Dice"]

# Avoid applying to these companies if they have these bad words in their 'Job Description' section...  (In development)
bad_words = str(os.getenv("BAD_WORDS")).split(",") if os.getenv("BAD_WORDS") else []                     # (dynamic multiple search) or leave empty as []. Case Insensitive. Ex: ["word_1", "phrase 1", "word word", "polygraph", "US Citizenship", "Security Clearance"]

# Do you have an active Security Clearance? (True for Yes and False for No)
security_clearance = str(os.getenv("SECURITY_CLEARANCE")).lower() == "true"         # True or False, Note: True or False are case-sensitive

# Do you have a Masters degree? (True for Yes and False for No). If True, the tool will apply to jobs containing the word 'master' in their job description and if it's experience required <= current_experience + 2 and current_experience is not set as -1. 
did_masters = str(os.getenv("DID_MASTERS")).lower() == "true"                 # True or False, Note: True or False are case-sensitive

# Avoid applying to jobs if their required experience is above your current_experience. (Set value as -1 if you want to apply to all ignoring their required experience...)
current_experience = int(os.getenv("TOTAL_EXPERIENCE"))             # Integers > -2 (Ex: -1, 0, 1, 2, 3, 4...)
##






