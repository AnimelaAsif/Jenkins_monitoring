import requests

JENKINS_URL = 'http://13.233.29.101:8080'
USERNAME = 'mohammedasif'
PASSWORD = 'Rmn@12345'
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
            f.write(response.text)     
        print("Response content written to api.log file.")
    else:
        print(f"Failed to retrieve build details. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Failed to connect to Jenkins: {e}")
