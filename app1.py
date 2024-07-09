import os
import requests
from requests.auth import HTTPBasicAuth

def fetch_latest_build_numbers(username, password, pipeline_name, count=18):
    jenkins_url = 'http://13.201.73.174:8080'
    job_url = f'{jenkins_url}/job/{pipeline_name}/api/json'
    auth = HTTPBasicAuth(username, password)
    
    try:
        response = requests.get(job_url, auth=auth)
        response.raise_for_status()
        job_info = response.json()
        builds = job_info['builds'][:count]
        build_numbers = sorted([build['number'] for build in builds])
        return build_numbers
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch Jenkins data: {e}")
        return []

def save_build_numbers_to_file(build_numbers, filename):
    try:
        with open(filename, 'w') as file:
            for number in build_numbers:
                file.write(f"{number}\n")
        print(f"Build numbers saved to {filename} successfully.")
    except IOError as e:
        print(f"Failed to write to {filename}: {e}")

def fetch_build_log(username, password, pipeline_name, build_number):
    jenkins_url = 'http://13.201.73.174:8080/'
    build_url = f'{jenkins_url}/job/{pipeline_name}/{build_number}/api/json'
    auth = HTTPBasicAuth(username, password)
    
    try:
        response = requests.get(build_url, auth=auth)
        response.raise_for_status()
        build_info = response.json()
        console_log_url = f"{build_info['url']}/api/json"
        console_log_response = requests.get(console_log_url, auth=auth)
        console_log_response.raise_for_status()
        console_log = console_log_response.text
        
        return console_log
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch build {build_number} log: {e}")
        return None

def save_build_log_to_file(log_data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(log_data)
        # print(f"Build log saved to {filename} successfully.")
    except IOError as e:
        print(f"Failed to write log to {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    username = 'mohammedasif'
    password = 'Rmn@73383271'
    pipeline_name = 'monitoring'
    filename = 'build_data.log'
    
    latest_builds = fetch_latest_build_numbers(username, password, pipeline_name)
    
    if latest_builds:
        # print(f"Latest {len(latest_builds)} build numbers of {pipeline_name}:")
        # print(latest_builds)
        save_build_numbers_to_file(latest_builds, filename)
        
        logs_folder = 'logs'
        os.makedirs(logs_folder, exist_ok=True)
        
        for build_number in latest_builds:
            log_data = fetch_build_log(username, password, pipeline_name, build_number)
            if log_data:
                log_filename = os.path.join(logs_folder, f"{build_number}.log")
                save_build_log_to_file(log_data, log_filename)
            else:
                print(f"Skipping build {build_number} log.")
    
    else:
        print("Failed to fetch build numbers.")
