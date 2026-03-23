import requests
import json
import os

# Fetch the API key securely from GitHub Secrets
api_key = os.environ.get("IPSTACK_API_KEY")

# The IPstack API endpoint (checking the server's own IP)
url = f"http://api.ipstack.com/check?access_key={api_key}"

try:
    # Send the GET request
    response = requests.get(url)
    
    # Check if the request was successful (200 OK)
    if response.status_code == 200:
        data = response.json()
        
        # Save the data to a JSON file
        with open('ip_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print("Success! Data fetched and saved to ip_data.json")
    else:
        print(f"Failed to fetch data. HTTP Status: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
