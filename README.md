# 11402_CS381_HW2_API_Fetcher

HW2: IPstack API Fetcher
This repository contains a Python script and a GitHub Actions workflow designed to automatically fetch IP geolocation data using the IPstack API.

Features
Automated Data Fetching: A GitHub Actions workflow (main.yml) runs daily at midnight UTC to retrieve the latest data.

Manual Execution: The workflow can also be triggered manually on-demand via the GitHub Actions interface.

Secure API Key Storage: Uses GitHub Repository Secrets to securely store the API access key, ensuring it is never exposed in the public code.

JSON Output: The retrieved geolocation data is saved as ip_data.json and uploaded as a downloadable GitHub Artifact.

Repository Structure
api.py: The core Python script. It uses the requests library to connect to the IPstack API, retrieves the executing server's IP data, and saves the output to a JSON file.

.github/workflows/main.yml: The YAML configuration file. It defines the GitHub Actions Ubuntu environment, sets up Python 3.10, handles dependencies, executes the script, and uploads the final artifact.

README.md: Project documentation.

Setup & Configuration
To execute this workflow, the IPstack API key must be configured in the repository's environment:

Go to Settings > Secrets and variables > Actions.

Click New repository secret.

Set the Name to: IPSTACK_API_KEY

Paste your IPstack access key into the Secret field and save.

How to Run
Navigate to the Actions tab in this repository.

Click on Daily IP API Fetcher in the left sidebar.

Click the Run workflow dropdown on the right side and click the green Run workflow button.

Once the job completes successfully, click into the run summary.

Scroll down to the Artifacts section and download the ip-geolocation-data zip file to view the generated ip_data.json file.
