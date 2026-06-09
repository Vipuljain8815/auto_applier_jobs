
###################################################### CONFIGURE YOUR TOOLS HERE ######################################################

import os
from config.env_loader import load_env

# Load environment variables from .env file
load_env(os.path.join(os.path.dirname(__file__), "..", ".env"))

# Login Credentials for LinkedIn (Optional)
linkedin_email_or_phone = os.getenv("LINKEDIN_EMAIL_OR_PHONE")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

# Login Credentials for Naukri
naukri_username = os.getenv("NAUKRI_USERNAME")
naukri_password = os.getenv("NAUKRI_PASSWORD")

# Login Credentials for Gmail Email Sender
gmail_username = os.getenv("GMAIL_USERNAME")
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")

## Artificial Intelligence (Beta Not-Recommended)
# Use AI
use_AI = str(os.getenv("USE_AI")).lower() == "true"                          # True or False, Note: True or False are case-sensitive

##> ------ Yang Li : MARKYangL - Feature ------
##> ------ Tim L : tulxoro - Refactor ------
# Select AI Provider
ai_provider = os.getenv("AI_PROVIDER")               # "openai", "deepseek", "gemini"



# Your LLM url or other AI api url and port
llm_api_url = "https://api.openai.com/v1/"       # Examples: "https://api.openai.com/v1/", "http://127.0.0.1:1234/v1/", "http://localhost:1234/v1/", "https://api.deepseek.com", "https://api.deepseek.com/v1"

# Your LLM API key or other AI API key 
llm_api_key = os.getenv("OPENAI_API_KEY", "not-needed")              # Enter your API key in the quotes, make sure it's valid, if not will result in error.

# Your LLM model name or other AI model name
llm_model = "gpt-5-mini"          # Examples: "gpt-3.5-turbo", "gpt-4o", "llama-3.2-3b-instruct", "qwen3:latest", "gemini-pro", "gemini-1.5-flash", "gemini-2.5-flash", "deepseek-llm:latest"

llm_spec = "openai"                # Examples: "openai", "openai-like", "openai-like-github", "openai-like-mistral"

# # Yor local embedding model name or other AI Embedding model name
# llm_embedding_model = "nomic-embed-text-v1.5"

# Do you want to stream AI output?
stream_output = False                    # Examples: True or False. (False is recommended for performance, True is recommended for user experience!)
##



