import csv
import os

path_applied = 'all excels/all_applied_applications_history.csv'
path_failed = 'all excels/all_failed_applications_history.csv'

if os.path.exists(path_applied):
    with open(path_applied, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    with open(path_applied, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Job ID', 'Title', 'Company', 'Job Link', 'External Job link', 'Date Applied']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

if os.path.exists(path_failed):
    with open(path_failed, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    with open(path_failed, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Job ID', 'Job Link', 'Date Tried', 'Assumed Reason']
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

print("Cleaned up CSVs!")
