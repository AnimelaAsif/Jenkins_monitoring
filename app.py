import requests
import json
JENKINS_URL = 'http://13.201.73.174:8080/'
USERNAME = 'mohammedasif'
PASSWORD = 'Rmn@73383271'
PIPELINE_NAME = 'monitoring'
BUILD_NUMBER = '7'
api_url = f"{JENKINS_URL}/job/{PIPELINE_NAME}/{BUILD_NUMBER}/api/json"
auth = (USERNAME, PASSWORD)
try:
    response = requests.get(api_url, auth=auth)
    if response.status_code == 200:
        build_details = response.json()
        build_id = build_details['id']    
        print(f"Build ID of build number {BUILD_NUMBER} in pipeline {PIPELINE_NAME} is: {build_id}")
        with open('api.log', 'w') as f:
            json.dump(build_details, f, indent=4)
        print("Pretty-printed JSON content written to api.log file.")
    else:
        print(f"Failed to retrieve build details. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Failed to connect to Jenkins: {e}")
