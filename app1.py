import requests
from requests.auth import HTTPBasicAuth

jenkins_url = 'http://13.201.188.119:8080'
pipeline_name = 'monitoring'

build_count = 18
api_endpoint = f"{jenkins_url}/job/{pipeline_name}/api/json"

username = 'mohammedasif'
password = 'Rmn@73383271'

try:
    response = requests.get(api_endpoint, 
                            auth=HTTPBasicAuth(username, password),
                            params={'tree': 'builds[number,timestamp,result]'})
    response.raise_for_status()
    pipeline_data = response.json()

    builds = pipeline_data['builds'][:build_count]
    
    print(f"Latest {len(builds)} builds of pipeline '{pipeline_name}':")
    for build in builds:
        build_number = build['number']
        build_timestamp = build['timestamp']
        build_result = build['result']
        
        print(f"Build #{build_number} | Result: {build_result} | Timestamp: {build_timestamp}")
        
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Jenkins API: {e}")
except KeyError:
    print("Unexpected response format from Jenkins API.")
