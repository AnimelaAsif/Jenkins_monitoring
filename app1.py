import requests
from requests.auth import HTTPBasicAuth

def fetch_latest_build_numbers(username, password, pipeline_name, count=18):
    jenkins_url = 'http://13.201.73.174:8080/'
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

if __name__ == "__main__":
    username = 'mohammedasif'
    password = 'Rmn@73383271'
    pipeline_name = 'monitoring'
    filename = 'build_numbers.log'
    
    latest_builds = fetch_latest_build_numbers(username, password, pipeline_name)
    
    if latest_builds:
        print(f"Latest {len(latest_builds)} build numbers of {pipeline_name}:")
        print(latest_builds)
        save_build_numbers_to_file(latest_builds, filename)
    else:
        print("Failed to fetch build numbers.")
