import requests
import json
import os
import csv

api_key = os.environ.get("IPSTACK_API_KEY")
url = f"http://api.ipstack.com/check?access_key={api_key}"

print(f"Attempting to fetch data from IPstack...")

try:
    response = requests.get(url)
    print(f"API Response Code: {response.status_code}") # This tells us if the key worked
    
    if response.status_code == 200:
        data = response.json()
        
        # Check if the API returned an internal error message (common with free keys)
        if "success" in data and data["success"] is False:
            print(f"API Error: {data['error']['info']}")
        else:
            # 1. Save as JSON
            with open('ip_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            # 2. Save as CSV
            with open('ip_data.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["IP", "Country", "City", "Latitude", "Longitude"])
                writer.writerow([data.get("ip"), data.get("country_name"), data.get("city"), data.get("latitude"), data.get("longitude")])
                
            print("Success! Both ip_data.json and ip_data.csv created.")
    else:
        print(f"HTTP Failure. Check your API key in GitHub Secrets.")
except Exception as e:
    print(f"Python Error: {e}")
