import requests
import json
import os

# User input for the issue ID
issue_id = input("Enter the JIRA issue ID (e.g., EDEV-10000): ")

url = f"https://journal.atlassian.net/rest/api/3/issue/{issue_id}"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer your_api_token"  # Replace 'your_api_token' with your JIRA API token
}

user = "vseth@journaltech.com"
pwd="your_api_token" # Replace 'your_api_token' with your JIRA API token
response = requests.get(url, headers=headers, auth=(user,pwd))

if response.status_code == 200:
    issue_data = response.json()
    # Path to save the file
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    folder_path = os.path.join(desktop_path, "edev-issues-json")
    # Check if the folder exists, and create it if it doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"{issue_id}.json")
    
    # Writing JSON data
    with open(file_path, 'w') as json_file:
        json.dump(issue_data, json_file, indent=4)
    
    print(f"Issue data saved to {file_path}")
else:
    print("Failed to fetch issue:", response.status_code)