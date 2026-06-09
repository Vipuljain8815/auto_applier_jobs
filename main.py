import sys
import argparse
import os
import json
from setup_cli import run_setup

PREFS_FILE = os.path.join(os.path.dirname(__file__), "user_preferences.json")

def main():
    parser = argparse.ArgumentParser(description="Unified Job Applier Bot")
    parser.add_argument("--platform", choices=["linkedin", "naukri", "both", "linkedin_feed"], help="Select which platform to run the bot on.")
    parser.add_argument("--update", action="store_true", help="Run the interactive setup to update your preferences.")
    args = parser.parse_args()

    if args.update or not os.path.exists(PREFS_FILE):
        run_setup()

    # Load preferences
    prefs = {}
    if os.path.exists(PREFS_FILE):
        with open(PREFS_FILE, "r") as f:
            prefs = json.load(f)

    from config.env_loader import load_env
    load_env()
    platform = args.platform or os.getenv("PLATFORM") or prefs.get("platform")
    
    if not platform:
        print("Which platform would you like to apply on?")
        print("1. LinkedIn")
        print("2. Naukri")
        print("3. Both")
        print("4. LinkedIn Feed Applier (Email applications)")
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice == "1":
            platform = "linkedin"
        elif choice == "2":
            platform = "naukri"
        elif choice == "3":
            platform = "both"
        elif choice == "4":
            platform = "linkedin_feed"
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)

    if platform in ["naukri", "both"]:
        print("--- Running Naukri Bot ---")
        try:
            from modules.naukri_main import main as run_naukri
            run_naukri()
        except Exception as e:
            print(f"Error running Naukri bot: {e}")

    if platform in ["linkedin", "both"]:
        print("--- Running LinkedIn Bot ---")
        try:
            from modules.linkedin_main import main as run_linkedin
            run_linkedin()
        except Exception as e:
            print(f"Error running LinkedIn bot: {e}")

    if platform == "linkedin_feed":
        print("--- Running LinkedIn Feed Applier ---")
        try:
            from modules.linkedin_feed_main import main as run_linkedin_feed
            run_linkedin_feed()
        except Exception as e:
            print(f"Error running LinkedIn Feed bot: {e}")

if __name__ == "__main__":
    main()
