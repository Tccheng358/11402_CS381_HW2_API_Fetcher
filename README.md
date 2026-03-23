# 11402_CS381_HW2_API_Fetcher

## Overview
A Python script and GitHub Actions workflow that automatically fetches IP geolocation data using the IPstack API.

## Features
- **Automated Data Fetching**: GitHub Actions workflow runs daily at midnight UTC
- **Manual Execution**: Trigger workflow on-demand via GitHub Actions interface
- **Secure API Key Storage**: Uses GitHub Repository Secrets to protect API credentials
- **JSON Output**: Geolocation data saved as `ip_data.json` and available as downloadable artifact

## Repository Structure
- `api.py` - Core Python script using requests library to fetch IP data from IPstack API
- `.github/workflows/main.yml` - GitHub Actions workflow configuration (Ubuntu, Python 3.10, dependencies, artifact upload)
- `README.md` - Project documentation

## Setup & Configuration
1. Go to **Settings > Secrets and variables > Actions**
2. Click **New repository secret**
3. Set Name to `IPSTACK_API_KEY`
4. Paste your IPstack access key and save

## How to Run
1. Navigate to the **Actions** tab
2. Select **Daily IP API Fetcher** from the sidebar
3. Click **Run workflow** dropdown and confirm
4. After completion, download the `ip-geolocation-data` artifact from the run summary
