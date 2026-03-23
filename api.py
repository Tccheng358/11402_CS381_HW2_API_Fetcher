import requests
import json
import os
import sys

# The .strip() removes any accidental spaces or newlines from the secret
api_key = os.environ.get("IPSTACK_API_KEY", "").strip()

url = f"http://api.ipstack.com/check?access_key={api_key}"

try:
    response = requests.get(url)
    data = response.json()
    
    # Debugging: This will help us see if the key is actually being pulled
    if not api_key:
        print("Error: IPSTACK_API_KEY is empty. Check GitHub Secrets.")
        sys.exit(1)

    if response.status_code == 200 and data.get("success") != False:
        with open('ip_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Success! Data fetched and saved to ip_data.json")
    else:
        error_msg = data.get('error', {}).get('info', f"HTTP {response.status_code}")
        print(f"API Error: {error_msg}")
        sys.exit(1)

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
