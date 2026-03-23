import requests
import json
import os
import csv

api_key = os.environ.get("IPSTACK_API_KEY")
url = f"http://api.ipstack.com/check?access_key={api_key}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # 1. Save as JSON
        with open('ip_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        # 2. Save as CSV (Flattening the data)
        with open('ip_data.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Writing Header
            writer.writerow(["IP", "Country", "City", "Latitude", "Longitude"])
            # Writing Data row
            writer.writerow([data.get("ip"), data.get("country_name"), data.get("city"), data.get("latitude"), data.get("longitude")])
            
        print("Success! Both JSON and CSV files saved.")
    else:
        print(f"Failed. Status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
